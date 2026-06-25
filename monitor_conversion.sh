#!/bin/bash
# Run from anywhere — uses absolute paths
DATA_DIR="/Users/dr.ajayshukla/harrison_app/data"
LOG_FILE="/Users/dr.ajayshukla/harrison_app/conversion_run.log"

echo "=== $(date) ==="
python3 - << PYEOF
import json, glob
done=0; desc=0
for f in glob.glob("$DATA_DIR/*.json"):
    try:
        d=json.load(open(f))
        for i in d.get('items',[]):
            t=i.get('type','')
            if t in ('why','how','shortanswer'): desc+=1
            if '-obj-' in i.get('id',''): done+=1
    except: pass
print(f"Converted: {done} objective | Remaining descriptive: {desc}")
PYEOF

echo "--- Recent log ---"
tail -8 "$LOG_FILE" 2>/dev/null | grep -v "^  File\|urllib\|http\|socket\|Timeout\|result ="

if ps aux | grep -q "[c]onvert_descriptive"; then
    echo "✅ Process RUNNING"
else
    echo "🏁 Process NOT running"
fi
