import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Instagram")
print(LOGO)
user = input(f"{PM} @username -> {RS}").strip()
try:
    r = requests.get(f"https://www.instagram.com/{user}/?__a=1", timeout=10)
    if r.status_code == 200:
        d = r.json().get("graphql",{}).get("user",{})
        print(f"\n{IN} {d.get('username','?')} | Followers: {d.get('edge_followed_by',{}).get('count',0)}")
    else:
        die("Not found")
except:
    die("Rate limited")
pause()
restart()
