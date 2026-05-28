import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Server Info")
print(LOGO)
inv = input(f"{PM} Invite -> {RS}").strip().split("/")[-1]
try:
    r = requests.get(f"https://discord.com/api/v9/invites/{inv}?with_counts=true", timeout=10)
    if r.status_code == 200:
        d = r.json(); g = d.get("guild",{})
        print(f"\n{IN} {g.get('name','?')} | Members:{d.get('approximate_member_count','?')} | Online:{d.get('approximate_presence_count','?')}")
    else:
        die("Bad invite")
except:
    die("Bad invite")
pause()
restart()
