import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("IP Lookup")
print(LOGO)
ip = input(f"{PM} IP -> {RS}").strip()
try:
    d = requests.get(f"https://ipapi.co/{ip}/json/", timeout=10).json()
    if not d.get("error"):
        print(f"\n{IN} {d['ip']} | {d.get('country_name','?')} | {d.get('city','?')} | {d.get('org','?')}")
    else:
        die("Bad IP")
except Exception as e:
    die(str(e))
pause()
restart()
