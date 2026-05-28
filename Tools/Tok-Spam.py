import sys, os, threading
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Token Spam")
print(LOGO)
token = input(f"{PM} Token -> {RS}").strip()
ch = input(f"\n{PM} Channel ID -> {RS}").strip()
msg = input(f"{PM} Message -> {RS}").strip()
def spam():
    while True:
        try:
            requests.post(f"https://discord.com/api/v9/channels/{ch}/messages",
                          json={"content":msg}, headers={"Authorization":token}, timeout=5)
        except: pass
for _ in range(3):
    threading.Thread(target=spam, daemon=True).start()
print(f"\n{IN} Spamming... Ctrl+C to stop")
try: time.sleep(99999)
except KeyboardInterrupt: pass
pause()
restart()
