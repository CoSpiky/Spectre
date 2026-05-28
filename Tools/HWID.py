import sys, os, subprocess, hashlib
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("HWID")
print(LOGO)
if OS_NAME != "Windows":
    die("Windows only")
try:
    cpu = subprocess.run("wmic cpu get processorid", shell=True, capture_output=True, text=True).stdout.split("\n")[1].strip()
    bios = subprocess.run("wmic bios get serialnumber", shell=True, capture_output=True, text=True).stdout.split("\n")[1].strip()
    disk = subprocess.run("wmic diskdrive get serialnumber", shell=True, capture_output=True, text=True).stdout.split("\n")[1].strip()
    mac = subprocess.run("getmac /nh", shell=True, capture_output=True, text=True).stdout.split("\n")[0].split()[0]
    hwid = hashlib.sha256(f"{cpu}{bios}{disk}{mac}".encode()).hexdigest()[:32]
    print(f"  CPU: {cpu}\n  BIOS: {bios}\n  Disk: {disk}\n  MAC: {mac}\n  HWID: {hwid}")
except Exception as e:
    die(str(e))
pause()
restart()
