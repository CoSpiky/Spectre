import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Dark Web Links")
print(LOGO)
onions = [
    ("DuckDuckGo","duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion"),
    ("Hidden Wiki","zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion")
]
for name, link in onions:
    print(f"  {name}: {link}")
print(f"\n{IN} Open in Tor Browser")
pause()
restart()
