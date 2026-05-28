import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("BTC Lookup")
print(LOGO)
addr = input(f"{PM} Address -> {RS}").strip()
try:
    r = requests.get(f"https://blockchain.info/rawaddr/{addr}", timeout=10).json()
    print(f"\n  Balance: {r.get('final_balance',0)/100000000:.8f} BTC")
    print(f"  TXs: {r.get('n_tx',0)}")
except:
    print(f"\n{ER} Invalid")
pause()
restart()
