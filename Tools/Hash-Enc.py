import sys, os, hashlib
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Hash Generator")
print(LOGO)
text = input(f"{PM} Text -> {RS}").strip()
print(f"\n  MD5:    {hashlib.md5(text.encode()).hexdigest()}")
print(f"  SHA1:   {hashlib.sha1(text.encode()).hexdigest()}")
print(f"  SHA256: {hashlib.sha256(text.encode()).hexdigest()}")
print(f"  SHA512: {hashlib.sha512(text.encode()).hexdigest()}")
pause()
restart()
