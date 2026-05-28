import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Web Info")
print(LOGO)
url = input(f"{PM} URL -> {RS}").strip()
try:
    r = requests.get(url, timeout=10)
    server = r.headers.get("Server","Unknown")
    print("\n" + IN + " " + W + str(r.status_code) + RS + " | " + server + " | {:.2f}s".format(r.elapsed.total_seconds()))
except Exception as e:
    die(str(e))
pause()
restart()
