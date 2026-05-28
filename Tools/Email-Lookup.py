import sys, os, socket
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Email Lookup")
print(LOGO)
email = input(f"{PM} Email -> {RS}").strip()
domain = email.split("@")[-1]
try:
    socket.getaddrinfo(domain, None)
    print(f"\n{IN} {domain} resolves")
except:
    print(f"\n{IN} {domain} does not resolve")
pause()
restart()
