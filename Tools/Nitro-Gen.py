import sys, os, random, string
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Nitro Gen")
print(LOGO)
n = int(input(f"{PM} Count -> {RS}"))
for _ in range(n):
    code = "".join(random.choices(string.ascii_letters+string.digits, k=16))
    print(f"  https://discord.gift/{code}")
print(f"\n{IN} All fake - prank only")
pause()
restart()
