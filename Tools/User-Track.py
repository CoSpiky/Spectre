import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Username Tracker")
print(LOGO)
user = input(f"{PM} Username -> {RS}").strip()
sites = [("GitHub","github.com"),("Twitter","x.com"),("Instagram","instagram.com"),
         ("Reddit","reddit.com/user"),("Twitch","twitch.tv"),("YouTube","youtube.com/@"),
         ("Steam","steamcommunity.com/id")]
for name, domain in sites:
    try:
        r = requests.head(f"https://{domain}/{user}", timeout=5)
        print(f"  {OK} {name}" if r.status_code == 200 else f"  {ER} {name}")
    except:
        print(f"  {ER} {name}")
pause()
restart()
