import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Phone Lookup")
print(LOGO)
phone = input(f"{PM} Phone -> {RS}").strip()
print(f"\n{IN} https://www.truecaller.com/search/{phone}")
pause()
restart()
