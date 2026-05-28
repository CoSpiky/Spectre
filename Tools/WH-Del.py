import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Delete Webhook")
print(LOGO)
w = input(f"{PM} Webhook URL -> {RS}").strip()
try:
    if requests.delete(w, timeout=10).status_code == 204:
        print(f"\n{OK} Deleted!")
    else:
        die("Failed")
except:
    die("Failed")
pause()
restart()
