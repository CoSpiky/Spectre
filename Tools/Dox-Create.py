import sys, os, json
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Dox Create")
print(LOGO)
d = {}
for field in ["name","age","address","phone","email","ip","social"]:
    d[field] = input(f"{PM} {field.title()} -> {RS}")
out = os.path.join(ROOT, "1-Output")
os.makedirs(out, exist_ok=True)
fp = os.path.join(out, f"dox_{d['name'].replace(' ','_')}.json")
with open(fp, "w") as f:
    json.dump(d, f, indent=2)
print(f"\n{OK} {fp}")
pause()
restart()
