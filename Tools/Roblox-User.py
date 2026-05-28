import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Roblox User")
print(LOGO)
user = input(f"{PM} Username -> {RS}").strip()
try:
    r = requests.post("https://users.roblox.com/v1/usernames/users",
                      json={"usernames":[user]}, timeout=10)
    data = r.json().get("data",[])
    if not data:
        die("Not found")
    uid = data[0]["id"]
    u = requests.get(f"https://users.roblox.com/v1/users/{uid}", timeout=10).json()
    fr = requests.get(f"https://friends.roblox.com/v1/users/{uid}/friends/count", timeout=10).json()
    print(f"\n{IN} {u['name']} | {u.get('displayName','?')} | Friends: {fr.get('count','?')}")
except Exception as e:
    die(str(e))
pause()
restart()
