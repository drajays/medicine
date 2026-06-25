#!/bin/bash
# Monitor conversion progress
echo "=== $(date) ==="
# Count total generated
python3 -c "
import json, glob
done=0; total=0
for f in glob.glob('data/*.json'):
    d=json.load(open(f))
    for i in d.get('items',[]):
        t = i.get('type','')
        if t in ('why','how','shortanswer'): total+=1
        if '-obj-' in i.get('id',''): done+=1
print(f'Converted: {done} objective | Descriptive: {total}')
"
# Last 5 lines of log
echo "--- Recent log ---"
tail -5 conversion_run.log 2>/dev/null
# Check if process still running
if ps aux | grep -q "[c]onvert_descriptive"; then
    echo "✅ Process running"
else
    echo "🏁 Process finished"
fi
