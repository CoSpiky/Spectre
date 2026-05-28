import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Token Clean")
print(LOGO)
token = input(f"{PM} Token -> {RS}").strip()
headers = {"Authorization": token}
try:
    for g in requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers, timeout=10).json():
        requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{g['id']}", headers=headers)
    for f in requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers, timeout=10).json():
        requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{f['id']}", headers=headers)
    print(f"\n{OK} Done!")
except Exception as e:
    die(str(e))
pause()
restart()
