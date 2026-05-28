import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Status Changer")
print(LOGO)
token = input(f"{PM} Token -> {RS}").strip()
status = input(f"\n{PM} Status (online/idle/dnd/invisible) -> {RS}").strip().lower()
custom = input(f"{PM} Custom text -> {RS}").strip()
d = {"status": status}
if custom:
    d["custom_status"] = {"text": custom}
try:
    r = requests.patch("https://discord.com/api/v9/users/@me/settings", json=d,
                       headers={"Authorization":token}, timeout=10)
    if r.status_code == 200:
        print(f"\n{OK} Changed!")
    else:
        print(f"\n{ER} Failed")
except Exception as e:
    die(str(e))
pause()
restart()
