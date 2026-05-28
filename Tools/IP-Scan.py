import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("IP Scan")
print(LOGO)
ip = input(f"{PM} IP -> {RS}").strip()
try:
    r = requests.get(f"http://ip-api.com/json/{ip}", timeout=10).json()
    if r.get("status") == "success":
        print(f"\n{IN} {r['query']} | {r['country']} | {r['city']} | {r['isp']}")
    else:
        die("Bad IP")
except Exception as e:
    die(str(e))
pause()
restart()
