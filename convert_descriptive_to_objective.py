#!/usr/bin/env python3
"""
convert_descriptive_to_objective.py
-------------------------------------
Reads all chapter JSON files in harrison_app/data/, finds items of type
'why', 'how', 'shortanswer', and uses a local Ollama model to generate
one objective question (MCQ, true_false, or assertion_reason) per item.

The original descriptive items are KEPT INTACT. New items are appended.

Usage:
    python3 convert_descriptive_to_objective.py [options]

Options:
    --dry-run    Print generated items without writing to disk
    --limit N    Only process at most N descriptive items (for testing)
    --file FILE  Process only a specific JSON file (basename)
    --model M    Ollama model to use (default: qwen3:14b)
"""

import json, glob, sys, os, re, time, argparse, hashlib, urllib.request

OLLAMA_URL   = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "qwen3:14b"
DATA_DIR     = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

SYSTEM_PROMPT = """You are a medical question writer for Harrison's Principles of Internal Medicine.
Given a descriptive Q&A, create ONE objective question.

Choose the BEST format:
- MCQ: single correct answer with 4 options (good distractors)
- true_false: clear factual statement
- assertion_reason: cause-effect concept

Output ONLY valid JSON, nothing else. No markdown, no thinking, no explanation.

MCQ format:
{"type":"mcq","stem":"Question?","options":["A","B","C","D"],"correctOption":0,"explanation":"Why correct"}

true_false format:
{"type":"true_false","statement":"Statement.","correctAnswer":true,"explanation":"Why"}

assertion_reason format:
{"type":"assertion_reason","assertion":"A statement.","reason":"R statement.","correctOption":0,"explanation":"..."}
correctOption meanings: 0=both true R explains A; 1=both true R doesn't explain A; 2=A true R false; 3=A false R true"""


def call_ollama(prompt: str, model: str) -> str:
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "system": SYSTEM_PROMPT,
        "stream": False,
        "options": {"temperature": 0.3, "num_predict": 600}
    }).encode()
    req = urllib.request.Request(OLLAMA_URL, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read()).get("response", "").strip()


def extract_json(text: str):
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
    # strip markdown fences
    text = re.sub(r'^```[a-z]*\n?', '', text).rstrip('`').strip()
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
        return (bool(obj.get("stem","").strip()) and
                isinstance(obj.get("options"), list) and len(obj["options"]) >= 2 and
                isinstance(obj.get("correctOption"), int))
    if t == "true_false":
        return (bool(obj.get("statement","").strip()) and
                isinstance(obj.get("correctAnswer"), bool))
    if t == "assertion_reason":
        return (bool(obj.get("assertion","").strip()) and
                bool(obj.get("reason","").strip()) and
                isinstance(obj.get("correctOption"), int))
    return False


def new_id(orig_id: str) -> str:
    h = hashlib.md5(orig_id.encode()).hexdigest()[:6]
    return f"{orig_id}-obj-{h}"


def already_done(items: list, orig_id: str) -> bool:
    prefix = orig_id + "-obj-"
    return any(i.get("id","").startswith(prefix) for i in items)


def process_file(filepath: str, model: str, dry_run: bool, limit: int, counter: list) -> int:
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
            print(f"  ⏭  {orig_id} (already done)")
            continue

        q = item.get("question") or item.get("stem", "")
        a = item.get("answer", "")
        if not q.strip():
            continue

        kp = item.get("keyPoints", [])
        kp_text = ("\nKey Points:\n" + "\n".join(f"- {p}" for p in kp)) if kp else ""
        prompt = f"Convert to ONE objective question.\n\nQuestion: {q}\n\nAnswer: {a}{kp_text}\n\nOutput ONLY JSON."

        print(f"  🔄 [{item['type']}] {orig_id[:55]} ...", end=" ", flush=True)
        try:
            raw = call_ollama(prompt, model)
        except Exception as e:
            print(f"❌ Ollama error: {e}")
            time.sleep(2)
            continue

        obj = extract_json(raw)
        if obj is None:
            print(f"⚠️  parse fail | raw: {raw[:120]}")
            continue
        if not validate(obj):
            print(f"⚠️  invalid structure: {obj}")
            continue

        obj["id"]             = new_id(orig_id)
        obj["subtopic"]       = item.get("subtopic", "")
        obj["_generatedFrom"] = orig_id

        new_items.append(obj)
        counter[0] += 1
        print(f"✅ {obj['type']}")
        time.sleep(0.2)

    if not new_items:
        return 0

    if dry_run:
        print(f"  [DRY RUN] {len(new_items)} new items — NOT written")
        for ni in new_items:
            print(f"    [{ni['type']}] {ni['id']}")
        return len(new_items)

    data["items"] = items + new_items
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  💾 Wrote {len(new_items)} items → {os.path.basename(filepath)}")
    return len(new_items)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--limit", type=int, default=0, help="Max items to process (0=all)")
    p.add_argument("--file", type=str, default="")
    p.add_argument("--model", type=str, default=DEFAULT_MODEL)
    args = p.parse_args()

    try:
        urllib.request.urlopen("http://localhost:11434/", timeout=3)
    except Exception:
        print("❌ Ollama not running. Start with: ollama serve")
        sys.exit(1)

    if args.file:
        path = args.file if os.path.isabs(args.file) else os.path.join(DATA_DIR, args.file)
        files = [path]
    else:
        files = sorted(glob.glob(os.path.join(DATA_DIR, "*.json")))

    print(f"📚 {len(files)} file(s) | 🤖 {args.model} | {'DRY RUN' if args.dry_run else 'WRITE MODE'}")
    print()

    total, counter = 0, [0]
    for fpath in files:
        if args.limit > 0 and counter[0] >= args.limit:
            print(f"\n🏁 Limit {args.limit} reached.")
            break
        try:
            with open(fpath, encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"⚠️  {os.path.basename(fpath)}: {e}")
            continue

        desc = [i for i in data.get("items",[]) if i.get("type") in ("why","how","shortanswer")]
        if not desc:
            continue

        done = sum(1 for i in desc if already_done(data.get("items",[]), i.get("id","")))
        todo = len(desc) - done
        if todo == 0:
            print(f"✓ {os.path.basename(fpath)}: all {len(desc)} already done")
            continue

        print(f"\n📄 {os.path.basename(fpath)} — {todo} to convert ({done} done already)")
        added = process_file(fpath, args.model, args.dry_run, args.limit, counter)
        total += added

    print(f"\n{'='*55}")
    print(f"✅ Done! Generated {total} new objective questions.")
    if not args.dry_run and total > 0:
        print("💡 Run: cd harrison_app/web && npm run build")

if __name__ == "__main__":
    main()
