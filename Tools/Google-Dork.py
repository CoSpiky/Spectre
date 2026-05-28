import sys, os, webbrowser
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Google Dork")
print(LOGO)
dorks = {
    "1": 'intitle:"admin panel"',
    "2": 'intext:"sql" "password" filetype:txt',
    "3": 'inurl:"view/index.shtml"',
    "4": 'intitle:"index of" "backup"',
    "5": 'inurl:login.jsp'
}
for k, v in dorks.items():
    print(f"  [{k}] {v}")
c = input(f"\n{PM} Choice -> {RS}")
if c in dorks:
    webbrowser.open(f"https://www.google.com/search?q={dorks[c]}")
else:
    bad()
pause()
restart()
