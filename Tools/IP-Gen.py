import sys, os, random
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("IP Gen")
print(LOGO)
n = int(input(f"{PM} Count -> {RS}"))
for _ in range(n):
    ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
    print(f"  {W}{ip}{RS}")
pause()
restart()
