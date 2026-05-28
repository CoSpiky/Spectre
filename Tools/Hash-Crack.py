import sys, os, hashlib
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Hash Cracker")
print(LOGO)
h = input(f"{PM} Hash -> {RS}").strip().lower()
t = input(f"{PM} Type (md5/sha1/sha256/sha512) -> {RS}").strip().lower()
w = input(f"{PM} Wordlist -> {RS}").strip()
algs = {"md5":hashlib.md5,"sha1":hashlib.sha1,"sha256":hashlib.sha256,"sha512":hashlib.sha512}
if t not in algs:
    die("Bad type")
with open(w, "r", errors="ignore") as f:
    for line in f:
        word = line.strip()
        if algs[t](word.encode()).hexdigest() == h:
            print(f"\n{OK} {word}")
            break
    else:
        print(f"\n{ER} Not found")
pause()
restart()
