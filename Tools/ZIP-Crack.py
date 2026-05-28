import sys, os
try:
    import pyzipper
except:
    print("pip install pyzipper")
    import sys; sys.exit(1)
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("ZIP Cracker")
print(LOGO)
z = input(f"{PM} ZIP file -> {RS}").strip()
w = input(f"{PM} Wordlist -> {RS}").strip()
if not os.path.exists(z) or not os.path.exists(w):
    die("Missing files")
with open(w, "r", errors="ignore") as f:
    pws = [l.strip() for l in f]
for p in pws:
    try:
        with pyzipper.AESZipFile(z) as zf:
            zf.setpassword(p.encode())
            zf.extractall(os.path.dirname(z))
        print(f"\n{OK} Password: {p}")
        break
    except:
        pass
else:
    print(f"\n{ER} Not found")
pause()
restart()
