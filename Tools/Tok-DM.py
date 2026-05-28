import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Mass DM")
print(LOGO)
token = input(f"{PM} Token -> {RS}").strip()
msg = input(f"\n{PM} Message -> {RS}").strip()
try:
    h = {"Authorization":token}
    fs = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=h, timeout=10).json()
    print(f"\n{WA} Sending to {len(fs)} friends...")
    for f in fs:
        try:
            dm = requests.post("https://discord.com/api/v9/users/@me/channels",
                               json={"recipient_id":f["id"]}, headers=h, timeout=5).json()
            requests.post(f"https://discord.com/api/v9/channels/{dm['id']}/messages",
                          json={"content":msg}, headers=h, timeout=5)
            print(f"  {OK} {f['user']['username']}")
            time.sleep(0.5)
        except: pass
    print(f"\n{OK} Done!")
except Exception as e:
    die(str(e))
pause()
restart()
