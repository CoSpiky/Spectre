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
    "01":("Web Vuln Scanner","Check security headers.\n\nUsage: Enter URL with https://"),
    "02":("Web Info","Server status and response time.\n\nUsage: Enter URL with https://"),
    "03":("URL Extractor","Extract links from webpage.\n\nUsage: Enter URL"),
    "04":("IP Scanner","Geolocation for any IP.\n\nUsage: Enter IP"),
    "05":("Port Scanner","Scan 20 common ports.\n\nUsage: Enter IP"),
    "06":("Ping","Continuous ping. Ctrl+C to stop.\n\nUsage: Enter IP"),
    "10":("Dox Create","Create dox file (JSON).\n\nUsage: Fill fields"),
    "11":("Dox Tracker","View saved dox files.\n\nUsage: Select number"),
    "12":("EXIF Viewer","Extract image metadata.\n\nUsage: Image path"),
    "13":("Google Dork","Advanced search queries.\n\nUsage: Select dork"),
    "14":("Username Tracker","Check 7+ platforms.\n\nUsage: Username"),
    "15":("Email Breach","HaveIBeenPwned check.\n\nUsage: Email"),
    "16":("Email Lookup","Verify email domain.\n\nUsage: Email"),
    "17":("Phone Lookup","Truecaller search.\n\nUsage: Phone number"),
    "18":("IP Lookup","Detailed IP info.\n\nUsage: IP"),
    "19":("Instagram","Public profile info.\n\nUsage: @username"),
    "20":("Phish Generator","Fake login page.\n\nUsage: Select template"),
    "21":("ZIP Cracker","Brute-force ZIP.\n\nUsage: ZIP + wordlist"),
    "22":("Hash Cracker","Crack hashes.\n\nUsage: Hash + type + wordlist"),
    "23":("Hash Generator","Generate hashes.\n\nUsage: Text"),
    "24":("Database Search","Breach database.\n\nUsage: Email/username"),
    "25":("Dark Web Links","Onion links.\n\nUsage: Tor Browser"),
    "26":("IP Generator","Random IPs.\n\nUsage: Count"),
    "30":("Payload Builder","Build test payload.\n\nUsage: Name + C2 URL"),
    "40":("Roblox Cookie","Login with cookie.\n\nUsage: .ROBLOSECURITY"),
    "41":("Cookie Info","Roblox account info.\n\nUsage: Cookie"),
    "42":("Roblox ID","Lookup by ID.\n\nUsage: User ID"),
    "43":("Roblox User","Lookup by username.\n\nUsage: Username"),
    "50":("Token Clean","Clean Discord token.\n\nUsage: Token"),
    "51":("Token Info","Discord account info.\n\nUsage: Token"),
    "52":("Token Join","Join server.\n\nUsage: Token + invite"),
    "53":("Token Leave","Leave server.\n\nUsage: Token + server ID"),
    "54":("Token Login","Browser login.\n\nUsage: Token"),
    "55":("Token Spam","Spam channel.\n\nUsage: Token + channel + msg"),
    "56":("Mass DM","Message friends.\n\nUsage: Token + message"),
    "57":("Status Changer","Change status.\n\nUsage: Token + status"),
    "60":("WiFi Collector","Saved WiFi passwords.\n\nUsage: Run"),
    "61":("History Grab","Browser history.\n\nUsage: Run"),
    "67b":("Bot Clean","Clean server.\n\nUsage: Bot token + server ID"),
    "70":("Nitro Gen","Fake Nitro codes.\n\nUsage: Count"),
    "71":("Webhook Info","Webhook details.\n\nUsage: Webhook URL"),
    "72":("Webhook Delete","Delete webhook.\n\nUsage: Webhook URL"),
    "73":("Webhook Spam","Spam webhook.\n\nUsage: URL + msg + threads"),
    "74":("Webhook Gen","Create webhook.\n\nUsage: Token + channel"),
    "75":("Server Info","Discord server info.\n\nUsage: Invite code"),
    "76":("Screenshot","Take screenshot.\n\nUsage: Run"),
    "80":("Keylogger","Log keystrokes.\n\nUsage: Run, Ctrl+C"),
    "81":("HWID","Hardware fingerprint.\n\nUsage: Run"),
    "82":("System Info","System specs.\n\nUsage: Run"),
    "100":("Wallet Finder","Crypto wallets.\n\nUsage: Run"),
    "101":("BTC Lookup","Bitcoin address.\n\nUsage: BTC address"),
    "104":("Fake TX","Fake transaction.\n\nUsage: Coin, amount, to"),
    "105":("System Test","Diagnostic tool.\n\nUsage: Run"),
    "110":("Info","Version and credits.\n\nUsage: Run")
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
    set_title(f"Spectre | {PAGES[page]['name']}")
    print(LOGO)
    print(f"{G}  Spectre {VERSION} | [N]ext [B]ack [Q]uit | Page {page+1}/{len(PAGES)}{RS}")
    print(f"  {G}{chr(9472)*75}{RS}")
    print(f"  {Y}[ {PAGES[page]['name'].upper()} ]{RS}\n")
    for tool_num in PAGES[page]["tools"]:
        tool_name = HELP.get(tool_num, ("?",""))[0]
        print(f"  {G}{tool_num}{W} {tool_name}")
    print(f"\n  {G}{chr(9472)*75}{RS}")
    print(f"  {W}Type number + ENTER = Launch{RS}")

def main():
    page = 0
    while True:
        show_page(page)
        choice = input(f"\n  {PM} Choice -> {RS}").strip().lower()
        if choice in ("n", "next"):
            page = (page + 1) % len(PAGES)
        elif choice in ("b", "back"):
            page = (page - 1) % len(PAGES)
        elif choice in ("q", "quit", "exit"):
            clear()
            sys.exit(0)
        elif choice.zfill(2) in TOOL_MAP:
            if choice.zfill(2) in HELP:
                clear()
                print(LOGO)
                title, desc = HELP[choice.zfill(2)]
                print(f"\n{G}{chr(9472)*60}{RS}\n{Y}  {title}{RS}\n{G}{chr(9472)*60}{RS}")
                print(f"{W}{desc}{RS}\n{G}{chr(9472)*60}{RS}")
                print(f"\n{W}  ENTER = Launch | 'back' = Cancel{RS}")
                if input(f"  {PM} ").strip().lower() == "back":
                    continue
            launch(f"{TOOL_MAP[choice.zfill(2)]}.py")
        else:
            bad()

if __name__ == "__main__":
    main()
