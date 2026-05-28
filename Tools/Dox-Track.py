import sys, os, json
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Dox Tracker")
print(LOGO)
out = os.path.join(ROOT, "1-Output")
if not os.path.exists(out):
    die("No dox files")
files = [f for f in os.listdir(out) if f.startswith("dox_")]
if not files:
    die("No dox files")
for i, fname in enumerate(files, 1):
    print(f"  [{i}] {fname}")
c = int(input(f"\n{PM} # -> {RS}")) - 1
if 0 <= c < len(files):
    with open(os.path.join(out, files[c])) as f:
        data = json.load(f)
    for k, v in data.items():
        print(f"  {k}: {v}")
pause()
restart()
