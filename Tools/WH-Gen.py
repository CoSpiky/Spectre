import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Webhook Gen")
print(LOGO)
token = input(f"{PM} Token -> {RS}").strip()
ch = input(f"\n{PM} Channel ID -> {RS}").strip()
name = input(f"{PM} Name -> {RS}").strip() or "Spectre"
try:
    r = requests.post(f"https://discord.com/api/v9/channels/{ch}/webhooks",
                      json={"name":name}, headers={"Authorization":token}, timeout=10)
    if r.status_code == 200:
        d = r.json()
        print(f"\n{OK} https://discord.com/api/webhooks/{d['id']}/{d['token']}")
    else:
        print(f"\n{ER} {r.json().get('message','?')}")
except Exception as e:
    die(str(e))
pause()
restart()
