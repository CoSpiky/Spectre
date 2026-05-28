import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Roblox ID")
print(LOGO)
uid = input(f"{PM} ID -> {RS}").strip()
try:
    r = requests.get(f"https://users.roblox.com/v1/users/{uid}", timeout=10)
    if r.status_code == 200:
        print(f"\n{IN} {r.json()['name']} | {r.json().get('displayName','?')}")
    else:
        die("Not found")
except:
    die("Not found")
pause()
restart()
