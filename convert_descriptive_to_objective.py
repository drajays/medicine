#!/usr/bin/env python3
"""
convert_descriptive_to_objective.py
-------------------------------------
Converts 'why', 'how', 'shortanswer' items in harrison_app/data/ JSON files
into objective questions (mcq / true_false / assertion_reason) using a local
Ollama model. Original items are NEVER modified. New items are appended.

The script is safe to re-run — already-converted items are detected by id
prefix and skipped automatically (idempotent).

Usage:
    python3 convert_descriptive_to_objective.py [options]

Options:
    --dry-run      Show what would be generated, write nothing
    --limit N      Stop after processing N new items (0 = no limit)
    --file FILE    Process only this file (basename or full path)
    --model M      Ollama model (default: qwen3:14b)
    --timeout S    Ollama request timeout in seconds (default: 180)
    --retries N    Max retries per item on timeout/error (default: 3)
"""

import json, glob, sys, os, re, time, argparse, hashlib, urllib.request, urllib.error

OLLAMA_URL    = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "qwen3:14b"
DATA_DIR      = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
LOG_FILE      = os.path.join(os.path.dirname(os.path.abspath(__file__)), "conversion_log.jsonl")

SYSTEM_PROMPT = """You are a medical question writer for Harrison's Principles of Internal Medicine.
Given a descriptive Q&A, output ONE objective question as JSON.

Choose the best format for the concept:
- mcq: best for specific facts with 4 plausible options
- true_false: best for clear factual statements
- assertion_reason: best for cause-effect relationships

RULES:
1. Output ONLY valid JSON — no markdown, no explanation, no <think> tags
2. Distractors must be plausible but clearly wrong
3. Keep clinical accuracy

MCQ:
{"type":"mcq","stem":"Question?","options":["A","B","C","D"],"correctOption":0,"explanation":"Brief reason"}

true_false:
{"type":"true_false","statement":"Statement.","correctAnswer":true,"explanation":"Brief reason"}

assertion_reason:
{"type":"assertion_reason","assertion":"A.","reason":"R.","correctOption":0,"explanation":"Brief reason"}
correctOption: 0=both true R explains A | 1=both true R doesn't explain | 2=A true R false | 3=A false R true"""


def call_ollama(prompt: str, model: str, timeout: int) -> tuple[str, str]:
    """Call Ollama and return (distillation_trace, response_text).
    
    Uses /no_think prefix for batch speed. The 'thinking' field from the
    Ollama API response is captured as distillation_trace (Glassbox Principle).
    When the model has no thinking output, distillation_trace is ''.
    """
    payload = json.dumps({
        "model": model,
        "prompt": "/no_think\n" + prompt,  # fast mode; thinking via API field below
        "system": SYSTEM_PROMPT,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 700,
            "num_ctx": 2048,
        }
    }).encode()
    req = urllib.request.Request(
        OLLAMA_URL, data=payload,
        headers={"Content-Type": "application/json"}, method="POST"
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        result = json.loads(r.read())
    # Ollama returns thinking content in a separate 'thinking' field for
    # models that support it (qwen3, deepseek-r1). This is the CoT trace.
    thinking = (result.get("thinking") or "").strip()
    response = (result.get("response") or "").strip()
    # Fallback: also try to extract <think> tags from response text itself
    if not thinking:
        m = re.search(r'<think>([\s\S]*?)</think>', response, re.IGNORECASE)
        if m:
            thinking = m.group(1).strip()
    return thinking, response



def extract_think(text: str) -> str:
    """Extract raw CoT reasoning from <think>...</think> block.
    Per the Glassbox Principle, this is NEVER discarded."""
    m = re.search(r'<think>([\s\S]*?)</think>', text, flags=re.IGNORECASE)
    return m.group(1).strip() if m else ""


def extract_json(text: str):
    """Parse JSON from model output, stripping think blocks and markdown fences."""
    # Strip think blocks AFTER we've already captured them separately
    text = re.sub(r'<think>[\s\S]*?</think>', '', text, flags=re.IGNORECASE).strip()
    # Strip markdown fences
    text = re.sub(r'^```[a-zA-Z]*\s*', '', text).rstrip('` \n').strip()
    try:
        return json.loads(text)
    except Exception:
        m = re.search(r'\{[\s\S]+\}', text)
        if m:
            try: return json.loads(m.group())
            except Exception: pass
    return None


def validate(obj: dict) -> bool:
    t = obj.get("type")
    if t == "mcq":
        return (isinstance(obj.get("stem"), str) and obj["stem"].strip()
                and isinstance(obj.get("options"), list) and len(obj["options"]) >= 2
                and isinstance(obj.get("correctOption"), int))
    if t == "true_false":
        return (isinstance(obj.get("statement"), str) and obj["statement"].strip()
                and isinstance(obj.get("correctAnswer"), bool))
    if t == "assertion_reason":
        return (isinstance(obj.get("assertion"), str) and obj["assertion"].strip()
                and isinstance(obj.get("reason"), str) and obj["reason"].strip()
                and isinstance(obj.get("correctOption"), int))
    return False


def stable_id(orig_id: str) -> str:
    h = hashlib.md5(orig_id.encode()).hexdigest()[:6]
    return f"{orig_id}-obj-{h}"


def already_done(items: list, orig_id: str) -> bool:
    prefix = orig_id + "-obj-"
    return any(i.get("id", "").startswith(prefix) for i in items)


def build_prompt(item: dict) -> str:
    q = item.get("question") or item.get("stem", "")
    a = item.get("answer", "")
    kp = item.get("keyPoints", [])
    kp_text = ("\nKey Points:\n" + "\n".join(f"- {p}" for p in kp)) if kp else ""
    return f"Convert to ONE objective exam question.\n\nQ: {q}\n\nA: {a}{kp_text}\n\nJSON only:"


def log_entry(entry: dict):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def process_file(filepath: str, model: str, dry_run: bool,
                 limit: int, counter: list, timeout: int, retries: int) -> int:
    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)

    items: list = data.get("items", [])
    if not items:
        return 0

    new_items = []
    for item in items:
        if limit > 0 and counter[0] >= limit:
            break

        if item.get("type") not in ("why", "how", "shortanswer"):
            continue

        orig_id = item.get("id", "")
        if already_done(items + new_items, orig_id):
            continue  # silent skip — already converted

        q = item.get("question") or item.get("stem", "")
        if not q.strip():
            continue

        print(f"  🔄 [{item['type']:11}] {orig_id[:52]} ...", end=" ", flush=True)

        obj = None
        distillation_trace = ""
        for attempt in range(1, retries + 1):
            try:
                distillation_trace, raw = call_ollama(build_prompt(item), model, timeout)
                obj = extract_json(raw)
                if obj and validate(obj):
                    break
                else:
                    if attempt < retries:
                        print(f"⚠️retry{attempt} ", end="", flush=True)
                        time.sleep(3)
            except (urllib.error.URLError, TimeoutError, OSError, Exception) as e:
                if attempt < retries:
                    print(f"⏱retry{attempt} ", end="", flush=True)
                    time.sleep(5)
                else:
                    print(f"❌ FAIL ({type(e).__name__}: {e})")
                    log_entry({"status":"error","id":orig_id,"error":str(e),"file":os.path.basename(filepath),"ts":time.time()})
                    obj = None

        if obj is None or not validate(obj):
            print("❌ skip")
            log_entry({"status":"invalid","id":orig_id,"file":os.path.basename(filepath),"ts":time.time()})
            continue

        obj["id"]                = stable_id(orig_id)
        obj["subtopic"]          = item.get("subtopic", "")
        obj["_generatedFrom"]    = orig_id
        obj["distillation_trace"] = distillation_trace  # Glassbox Principle: raw CoT preserved

        new_items.append(obj)
        counter[0] += 1
        print(f"✅ {obj['type']}")
        log_entry({"status":"ok","id":obj["id"],"type":obj["type"],"from":orig_id,
                   "file":os.path.basename(filepath),"ts":time.time()})
        time.sleep(0.5)

    if not new_items:
        return 0

    if dry_run:
        print(f"  [DRY RUN] {len(new_items)} items — not written")
        for ni in new_items:
            print(f"    [{ni['type']}] {ni['id']}")
        return len(new_items)

    data["items"] = items + new_items
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  💾 {len(new_items)} items written → {os.path.basename(filepath)}")
    return len(new_items)


def main():
    p = argparse.ArgumentParser(description="Descriptive → Objective Q converter via Ollama")
    p.add_argument("--dry-run",  action="store_true",    help="Preview only, no writes")
    p.add_argument("--limit",    type=int, default=0,    help="Max new items to generate (0=all)")
    p.add_argument("--file",     type=str, default="",   help="Process only this file")
    p.add_argument("--model",    type=str, default=DEFAULT_MODEL)
    p.add_argument("--timeout",  type=int, default=180,  help="Ollama timeout seconds")
    p.add_argument("--retries",  type=int, default=3,    help="Retries per item")
    args = p.parse_args()

    # Verify Ollama is alive
    try:
        urllib.request.urlopen("http://localhost:11434/", timeout=5)
    except Exception:
        print("❌ Ollama not running! Start with: ollama serve")
        sys.exit(1)

    if args.file:
        path = args.file if os.path.isabs(args.file) else os.path.join(DATA_DIR, args.file)
        files = [path]
    else:
        files = sorted(glob.glob(os.path.join(DATA_DIR, "*.json")))

    print(f"\n{'='*60}")
    print(f"🤖 Model   : {args.model}")
    print(f"📁 Files   : {len(files)}")
    print(f"⏱  Timeout : {args.timeout}s  |  🔁 Retries: {args.retries}")
    print(f"{'🔍 DRY RUN' if args.dry_run else '✏️  WRITE MODE'}")
    print(f"{'='*60}\n")

    total, counter = 0, [0]
    start_time = time.time()

    for fpath in files:
        if args.limit > 0 and counter[0] >= args.limit:
            print(f"\n🏁 Limit of {args.limit} reached.")
            break

        try:
            with open(fpath, encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"⚠️  {os.path.basename(fpath)}: {e}")
            continue

        desc  = [i for i in data.get("items", []) if i.get("type") in ("why","how","shortanswer")]
        if not desc:
            continue

        done  = sum(1 for i in desc if already_done(data.get("items",[]), i.get("id","")))
        todo  = len(desc) - done
        if todo == 0:
            continue   # silent skip fully-done files

        elapsed = int(time.time() - start_time)
        print(f"📄 {os.path.basename(fpath):55}  [{done}/{len(desc)} done]  ⏱{elapsed}s")

        added  = process_file(fpath, args.model, args.dry_run,
                              args.limit, counter, args.timeout, args.retries)
        total += added

    elapsed = int(time.time() - start_time)
    print(f"\n{'='*60}")
    print(f"✅ Complete!  Generated: {total}  |  Time: {elapsed}s ({elapsed//60}m {elapsed%60}s)")
    if not args.dry_run and total > 0:
        print("💡 Now run:  cd harrison_app/web && npm run build")
    print(f"📋 Log: {LOG_FILE}")

if __name__ == "__main__":
    main()
