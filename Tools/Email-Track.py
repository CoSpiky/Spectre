import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Email Breach")
print(LOGO)
email = input(f"{PM} Email -> {RS}").strip()
try:
    r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}",
                      headers={"hibp-api-key":"none"}, timeout=10)
    if r.status_code == 200:
        breaches = r.json()
        print(f"\n{R}[BREACHED]{W} {len(breaches)} breaches:")
        for b in breaches:
            print(f"  {b['Name']}")
    elif r.status_code == 404:
        print(f"\n{G}[SAFE]")
    else:
        print(f"\n{IN} Rate limited")
except:
    print(f"\n{IN} Rate limited")
pause()
restart()
