import sys, os, socket, threading
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Port Scanner")
print(LOGO)
target = input(f"{PM} IP -> {RS}").strip()
open_ports = []
def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    if sock.connect_ex((target, port)) == 0:
        open_ports.append(port)
    sock.close()
ports = [21,22,23,25,53,80,110,135,139,143,443,445,993,995,1723,3306,3389,5900,8080,8443]
threads = []
for p in ports:
    t = threading.Thread(target=scan_port, args=(p,))
    t.start()
    threads.append(t)
    time.sleep(0.1)
for t in threads:
    t.join()
if open_ports:
    for p in sorted(open_ports):
        print(f"  {OK} Port {p}")
else:
    print(f"  {IN} No open ports")
pause()
restart()
