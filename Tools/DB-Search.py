import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Database Search")
print(LOGO)
q = input(f"{PM} Email/Username -> {RS}").strip()
try:
    r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{q}",
                      headers={"hibp-api-key":"none"}, timeout=10)
    if r.status_code == 200:
        for b in r.json():
            print(f"  {b['Name']}")
    else:
        print(f"\n{IN} Not found")
except:
    print(f"\n{IN} Try dehashed.com")
pause()
restart()
