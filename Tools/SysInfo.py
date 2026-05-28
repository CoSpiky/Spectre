import sys, os, platform, subprocess
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("System Info")
print(LOGO)
print(f"\n  OS: {platform.platform()}")
print(f"  Host: {platform.node()}")
print(f"  CPU: {platform.processor()}")
print(f"  User: {os.getenv('USERNAME','?')}")
try:
    gpu = subprocess.run("wmic path win32_videocontroller get caption", shell=True, capture_output=True, text=True).stdout.split("\n")[1].strip()
    print(f"  GPU: {gpu}")
except: pass
pause()
restart()
