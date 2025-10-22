import requests
import time
import os
import random
from colorama import Fore, init

# Initialize colorama for colored text
init(autoreset=True)

# Banner
BANNER = f"""
{Fore.RED}╔════════════════════════════════════════════════╗
{Fore.RED}║                                                ║
{Fore.RED}║            {Fore.WHITE}🚀 TIKTOK PRANK {Fore.RED}🚀           ║
{Fore.RED}║         {Fore.YELLOW}(Pro Version - Authenticated)          {Fore.RED}║
{Fore.RED}║                                                ║
{Fore.RED}╚════════════════════════════════════════════════╝
"""

# Pro Version Ad
PRO_AD = f"""
{Fore.GREEN}🔥 {Fore.CYAN}PRO VERSION ACTIVATED {Fore.RED}FEATURES {Fore.CYAN}ENABLED! 🔥
{Fore.YELLOW}✅ Private Proxy Support (HTTPS)
{Fore.YELLOW}✅ Multiple User-Agent Rotation
{Fore.YELLOW}✅ Authenticated Sessions
{Fore.YELLOW}✅ Auto Fallback Direct Connection
{Fore.YELLOW}✅ Enhanced Success Rate
{Fore.RED}📢 Telegram Contact: {Fore.WHITE}@vintok666    {Fore.RED}Link: {Fore.WHITE}https://t.me/vintok666
"""

proxy_error_count = 0
use_proxy = True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_user_agents():
    try:
        with open('user-agents.txt', 'r') as f:
            agents = [line.strip() for line in f if line.strip()]
        return agents if agents else ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"]
    except:
        return ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"]

def load_proxies():
    try:
        with open('data.txt', 'r') as f:
            proxies = [line.strip() for line in f if line.strip()]
        return proxies
    except:
        return []

def get_cookies():
    return {
        "sessionid": "a1e224f70b36d1009f1efd943e3bd60e",
        "mstoken": "fiKt2usrQKJQ_H5Jp8upVjKfbCzwkkWq0CEpAuOFEx0eU7IJRCSy9gX75RX5JJMk50yFXjmHvvdArF3xUy8V5SvzpZVqPFg7ca2O-RcLDq29ky9lsH3gPWWCMi6eD3qKQ7WXuHB0n5gQu4TFYzNBJzamfYw=",
        "ttwid": "1%7Cb_fZAN6DSI4LYebzqFY-tHuajiXLYvJ_yPGl7I-Dxmk%7C1761120429%7Cf174400fa63dc29c337ac8804a19f70fdfef5847939a75b86e3cda70a0548542",
        "passport_csrf_token": "de1a067c73bfa1f4976dc716e4dab0ca"
    }

def report_user(user_id, reason=90097, delay=5, user_agents=None, proxies=None):
    global proxy_error_count, use_proxy
    
    if not user_agents:
        user_agents = load_user_agents()
    
    headers = {
        "User-Agent": random.choice(user_agents),
        "Referer": f"https://www.tiktok.com/@{user_id}",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Origin": "https://www.tiktok.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }
    
    cookies = get_cookies()
    
    params = {
        "aid": 1988,
        "app_language": "en",
        "report_type": "user",
        "object_id": user_id,
        "reason": reason,
    }
    
    proxy_dict = None
    connection_type = f"{Fore.CYAN}Direct Connection"
    
    if use_proxy and proxies and len(proxies) > 0:
        proxy = random.choice(proxies)
        if not proxy.startswith('http'):
            proxy = f"https://{proxy}"
        proxy_dict = {"https": proxy, "http": proxy}
        connection_type = f"{Fore.YELLOW}Proxy"
    
    try:
        response = requests.post(
            "https://www.tiktok.com/api/report/",
            params=params,
            headers=headers,
            cookies=cookies,
            proxies=proxy_dict,
            timeout=15,
            verify=False
        )
        print(f"{Fore.GREEN}[+] Reported {Fore.WHITE}@{user_id} {Fore.GREEN}| Status: {response.status_code} | Mode: {connection_type} {Fore.GREEN}| Auth: {Fore.YELLOW}Logged In")
        proxy_error_count = 0
        time.sleep(delay)
        return True
    except (requests.exceptions.ProxyError, requests.exceptions.ConnectionError) as e:
        if use_proxy:
            proxy_error_count += 1
            print(f"{Fore.RED}[-] Proxy Error ({proxy_error_count}/3): {str(e)[:50]}...")
            
            if proxy_error_count >= 3:
                use_proxy = False
                print(f"{Fore.YELLOW}[!] Proxy disabled! Switching to direct connection...")
                return report_user(user_id, reason, 0, user_agents, proxies)
        else:
            print(f"{Fore.RED}[-] Connection Error: {str(e)[:50]}...")
        return False
    except Exception as e:
        print(f"{Fore.RED}[-] Error: {str(e)[:50]}...")
        return False

def main():
    global proxy_error_count, use_proxy
    
    clear_screen()
    print(BANNER)
    print(PRO_AD)
    
    user_agents = load_user_agents()
    proxies = load_proxies()
    
    print(f"{Fore.CYAN}[i] Loaded {len(user_agents)} user agents")
    print(f"{Fore.CYAN}[i] Loaded {len(proxies)} proxies")
    print(f"{Fore.GREEN}[i] Authentication: Active")
    print(f"{Fore.GREEN}[i] Proxy Mode: {'Enabled' if len(proxies) > 0 else 'Disabled (No proxies found)'}\n")
    
    if len(proxies) == 0:
        use_proxy = False
    
    target = input(f"{Fore.CYAN}[?] Enter TikTok Username to Report: {Fore.WHITE}@").strip()
    delay = int(input(f"{Fore.CYAN}[?] Delay between reports (seconds): {Fore.WHITE}") or 5)
    count = int(input(f"{Fore.CYAN}[?] Number of reports: {Fore.WHITE}") or 1)
    
    print(f"\n{Fore.YELLOW}[~] Starting reports for @{target}...\n")
    
    success = 0
    failed = 0
    
    for i in range(count):
        if report_user(target, delay=delay, user_agents=user_agents, proxies=proxies):
            success += 1
        else:
            failed += 1
        
        mode = f"{Fore.YELLOW}Proxy" if use_proxy else f"{Fore.CYAN}Direct"
        print(f"{Fore.BLUE}[{i+1}/{count}] Success: {Fore.GREEN}{success} {Fore.BLUE}| Failed: {Fore.RED}{failed} {Fore.BLUE}| Mode: {mode}")
        
        if i < count - 1:
            print(f"{Fore.BLUE}Waiting {delay} seconds...\n")
    
    print(f"\n{Fore.GREEN}╔══════════════════════════════════════╗")
    print(f"{Fore.GREEN}║ {Fore.WHITE}REPORT SUMMARY                      {Fore.GREEN}║")
    print(f"{Fore.GREEN}╠══════════════════════════════════════╣")
    print(f"{Fore.GREEN}║ {Fore.CYAN}Target    : {Fore.WHITE}@{target:<22}{Fore.GREEN}║")
    print(f"{Fore.GREEN}║ {Fore.CYAN}Total     : {Fore.WHITE}{count:<26}{Fore.GREEN}║")
    print(f"{Fore.GREEN}║ {Fore.CYAN}Success   : {Fore.GREEN}{success:<26}{Fore.GREEN}║")
    print(f"{Fore.GREEN}║ {Fore.CYAN}Failed    : {Fore.RED}{failed:<26}{Fore.GREEN}║")
    mode_final = "Direct Connection" if not use_proxy else "Proxy"
    print(f"{Fore.GREEN}║ {Fore.CYAN}Final Mode: {Fore.YELLOW}{mode_final:<22}{Fore.GREEN}║")
    print(f"{Fore.GREEN}╚══════════════════════════════════════╝")

if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()
