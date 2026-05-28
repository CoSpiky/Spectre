
from Core.Engine import *

TOOL_MAP = {
    "01":"Web-Vuln","02":"Web-Info","03":"Web-URL","04":"IP-Scan","05":"IP-Port","06":"IP-Ping",
    "10":"Dox-Create","11":"Dox-Track","12":"Img-Exif","13":"Google-Dork",
    "14":"User-Track","15":"Email-Track","16":"Email-Lookup","17":"Phone-Lookup",
    "18":"IP-Lookup","19":"Insta-Account","20":"Phish","21":"ZIP-Crack",
    "22":"Hash-Crack","23":"Hash-Enc","24":"DB-Search","25":"Dark-Web","26":"IP-Gen",
    "30":"Payload-Build","40":"Roblox-Cookie","41":"Roblox-Cookie-Info","42":"Roblox-ID",
    "43":"Roblox-User","50":"Tok-Clean","51":"Tok-Info","52":"Tok-Join","53":"Tok-Leave",
    "54":"Tok-Login","55":"Tok-Spam","56":"Tok-DM","57":"Tok-Status",
    "60":"WiFi-Collect","61":"History-Grab","67b":"Bot-Clean","70":"Nitro-Gen",
    "71":"WH-Info","72":"WH-Del","73":"WH-Spam","74":"WH-Gen","75":"Srv-Info",
    "76":"SS-Grab","80":"Key-Log","81":"HWID","82":"SysInfo",
    "100":"Wallet-Find","101":"BTC-Lookup","104":"Fake-TX","105":"System-Test","110":"Info"
}

HELP = {
    "01":("Web Vuln Scanner","Check security headers on a website."),
    "02":("Web Info","Get server info and response time."),
    "04":("IP Scanner","Geolocation lookup for any IP."),
    "05":("Port Scanner","Scan 20 common ports on a target."),
    "14":("Username Tracker","Check username on 7+ platforms."),
    "15":("Email Breach Check","Check HaveIBeenPwned."),
    "22":("Hash Cracker","Crack hashes with wordlist."),
    "23":("Hash Generator","Generate MD5/SHA hashes."),
    "25":("Dark Web Links","Verified .onion links."),
    "30":("Payload Builder","Build test payloads."),
    "51":("Token Info","Discord token details."),
    "60":("WiFi Collector","Collect saved WiFi passwords."),
    "81":("HWID","Generate hardware fingerprint."),
    "82":("System Info","OS and hardware specs."),
    "101":("BTC Lookup","Bitcoin address info."),
    "110":("Info","Spectre version info.")
}

PAGES = [
    {"name":"Network & OSINT","tools":["01","02","03","04","05","06","10","11","12","13","14","15","16","17","18","19"]},
    {"name":"Attacks & Cracking","tools":["20","21","22","23","24","25","26","30"]},
    {"name":"Roblox","tools":["40","41","42","43"]},
    {"name":"Discord","tools":["50","51","52","53","54","55","56","57","67b","70","71","72","73","74","75"]},
    {"name":"Surveillance","tools":["60","61","76","80"]},
    {"name":"System","tools":["81","82","100","101","104","105","110"]},
]

def show_page(page):
    clear()
    set_title(f"Spectre | {PAGES[page][\"name\"]}")
    print(LOGO)
    print(f"{G}  Spectre {VERSION} | [N]ext [B]ack [Q]uit | Page {page+1}/{len(PAGES)}{RS}")
    print(f"  {G}{chr(9472)*75}{RS}")
    print(f"  {Y}[ {PAGES[page][\"name\"].upper()} ]{RS}\\n")
    for tool_num in PAGES[page]["tools"]:
        tool_name = HELP.get(tool_num, ("?",""))[0]
        print(f"  {G}{tool_num}{W} {tool_name}")
    print(f"\\n  {G}{chr(9472)*75}{RS}")
    print(f"  {W}Type number + ENTER = Launch{RS}")

def main():
    page = 0
    while True:
        show_page(page)
        choice = input(f"\\n  {PM} Choice -> {RS}").strip().lower()
        if choice in ("n", "next"): page = (page + 1) % len(PAGES)
        elif choice in ("b", "back"): page = (page - 1) % len(PAGES)
        elif choice in ("q", "quit", "exit"): clear(); sys.exit(0)
        elif choice.zfill(2) in TOOL_MAP: launch(f"{TOOL_MAP[choice.zfill(2)]}.py")
        else: bad()

if __name__ == "__main__":
    main()
