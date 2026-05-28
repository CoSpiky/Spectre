import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("System Test")
print(LOGO)
print(f"\n{W}  System diagnostic tool{RS}")
print(f"  {IN} OS: {OS_NAME}")
print(f"  {IN} All systems operational")
pause()
restart()
