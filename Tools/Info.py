import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Info")
print(LOGO)
print(f"\n{W}  Spectre {VERSION}\n  {AUTHOR} | {PLATFORM}\n  Research framework.{RS}")
pause()
restart()
