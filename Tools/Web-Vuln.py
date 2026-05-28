import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Web Vuln")
print(LOGO)
url = input(f"{PM} URL -> {RS}").strip()
if not url.startswith("http"):
    die("Invalid URL")
try:
    r = requests.get(url, timeout=10)
    checks = [("X-Frame-Options","Clickjack"),("Content-Security-Policy","XSS"),("Strict-Transport-Security","MitM")]
    for h, risk in checks:
        if h in r.headers:
            print("  " + G + "[OK]" + W + " " + h)
        else:
            print("  " + R + "[VULN]" + W + " Missing " + h + " (" + risk + ")")
except Exception as e:
    die(str(e))
pause()
restart()
