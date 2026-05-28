import sys, os, re
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("URL Extractor")
print(LOGO)
url = input(f"{PM} URL -> {RS}").strip()
try:
    r = requests.get(url, timeout=10)
    links = re.findall(r'href=[\x27\x22]?([^\x27\x22 >]+)', r.text)
    print(f"\n{IN} {len(links)} links (first 20):")
    for l in links[:20]:
        print("  " + W + l + RS)
except Exception as e:
    die(str(e))
pause()
restart()
