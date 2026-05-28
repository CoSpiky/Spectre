import sys, os, subprocess, re
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("WiFi Collector")
print(LOGO)
if OS_NAME != "Windows":
    die("Windows only")
try:
    profiles = subprocess.run("netsh wlan show profiles", shell=True, capture_output=True, text=True).stdout
    ssids = re.findall(r"All User Profile\s*:\s*(.*)", profiles)
    for ssid in ssids:
        ssid = ssid.strip()
        det = subprocess.run(f'netsh wlan show profile "{ssid}" key=clear', shell=True, capture_output=True, text=True).stdout
        pw = re.findall(r"Key Content\s*:\s*(.*)", det)
        if pw:
            print(f"  {OK} {ssid}: {pw[0]}")
        else:
            print(f"  {ER} {ssid}")
except Exception as e:
    die(str(e))
pause()
restart()
