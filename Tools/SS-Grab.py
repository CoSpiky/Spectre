import sys, os
from PIL import ImageGrab
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Screenshot")
print(LOGO)
try:
    img = ImageGrab.grab()
    out = os.path.join(ROOT, "1-Output")
    os.makedirs(out, exist_ok=True)
    fp = os.path.join(out, f"ss_{int(time.time())}.png")
    img.save(fp)
    print(f"{OK} {fp}")
except Exception as e:
    die(str(e))
pause()
restart()
