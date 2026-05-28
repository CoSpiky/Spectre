import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Ping")
print(LOGO)
target = input(f"{PM} IP -> {RS}").strip()
if OS_NAME == "Windows":
    os.system(f"ping {target} -t")
else:
    os.system(f"ping {target}")
pause()
restart()
