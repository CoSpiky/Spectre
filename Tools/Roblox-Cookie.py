import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Roblox Cookie")
print(LOGO)
ck = input(f"{PM} Cookie -> {RS}").strip()
try:
    r = requests.get("https://www.roblox.com/mobileapi/userinfo",
                      cookies={".ROBLOSECURITY":ck}, timeout=10)
    if r.status_code == 200:
        u = r.json()
        print(f"\n{OK} {u['UserName']} | ID:{u['UserID']} | R$:{u.get('RobuxBalance','?')}")
    else:
        die("Bad cookie")
except:
    die("Bad cookie")
pause()
restart()
