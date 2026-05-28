import sys, os, random, datetime
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Fake TX")
print(LOGO)
coin = input(f"{PM} Coin -> {RS}").strip().upper()
amount = input(f"{PM} Amount -> {RS}").strip()
recipient = input(f"{PM} To -> {RS}").strip()
txid = "".join(random.choices("0123456789abcdef", k=64))
print(f"\n  Coin: {coin}\n  Amount: {amount}\n  To: {recipient}\n  TXID: {txid}\n  Time: {datetime.datetime.now()}")
print(f"\n{IN} Not a real transaction")
pause()
restart()
