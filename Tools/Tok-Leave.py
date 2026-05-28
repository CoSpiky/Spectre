import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Token Leave")
print(LOGO)
token = input(f"{PM} Token -> {RS}").strip()
gid = input(f"\n{PM} Server ID -> {RS}").strip()
try:
    r = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{gid}", headers={"Authorization":token}, timeout=10)
    if r.status_code == 204:
        print(f"\n{OK} Left!")
    else:
        print(f"\n{ER} Failed")
except Exception as e:
    die(str(e))
pause()
restart()
