import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Token Login")
print(LOGO)
token = input(f"{PM} Token -> {RS}").strip()
try:
    r = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization":token}, timeout=10)
    if r.status_code == 200:
        u = r.json()
        print(f"\n{OK} {u['username']}#{u.get('discriminator','0')}")
        scr = f'javascript:(function(){{var i=document.createElement("iframe");i.style.display="none";document.body.appendChild(i);i.contentWindow.localStorage.token="{token}";location.reload();}})();'
        print(f"\n{IN} Browser script:\n{scr}")
    else:
        die("Bad token")
except:
    die("Bad token")
pause()
restart()
