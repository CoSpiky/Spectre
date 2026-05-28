import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Webhook Info")
print(LOGO)
w = input(f"{PM} Webhook URL -> {RS}").strip()
try:
    r = requests.get(w, timeout=10)
    if r.status_code == 200:
        d = r.json()
        print(f"\n{IN} {d.get('name','?')} | Ch:{d['channel_id']} | Guild:{d.get('guild_id','?')}")
    else:
        die("Bad webhook")
except:
    die("Bad webhook")
pause()
restart()
