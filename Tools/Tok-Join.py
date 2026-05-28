import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Token Join")
print(LOGO)
token = input(f"{PM} Token -> {RS}").strip()
inv = input(f"\n{PM} Invite code -> {RS}").strip().split("/")[-1]
try:
    r = requests.post(f"https://discord.com/api/v9/invites/{inv}", headers={"Authorization":token}, timeout=10)
    if r.status_code == 200:
        print(f"\n{OK} Joined!")
    else:
        print(f"\n{ER} {r.json().get('message','?')}")
except Exception as e:
    die(str(e))
pause()
restart()
