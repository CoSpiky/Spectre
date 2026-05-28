import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Wallet Finder")
print(LOGO)
wallets = [
    ("Exodus","%APPDATA%\\Exodus"),
    ("Electrum","%APPDATA%\\Electrum"),
    ("BitcoinCore","%APPDATA%\\Bitcoin")
]
found = []
for name, p in wallets:
    ep = os.path.expandvars(p)
    if os.path.exists(ep):
        found.append(name)
        print(f"  {OK} {name}")
print(f"\n{OK} {len(found)} wallets!" if found else f"\n{IN} None found")
pause()
restart()
