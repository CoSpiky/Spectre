import sys, os
from PIL import Image
from PIL.ExifTags import TAGS
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("EXIF Viewer")
print(LOGO)
path = input(f"{PM} Image path -> {RS}").strip()
if not os.path.exists(path):
    die("Not found")
try:
    img = Image.open(path)
    ex = img._getexif()
    if ex:
        for tag, value in ex.items():
            name = TAGS.get(tag, tag)
            print(f"  {W}{name}:{RS} {value}")
    else:
        print(f"\n{IN} No EXIF data")
except Exception as e:
    die(str(e))
pause()
restart()
