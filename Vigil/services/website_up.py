import time
import requests
from urllib.parse import urlparse

import functions.colors as color
from functions.validate_url import validate_url
from functions.clear_terminal import clear_terminal

def isUp(url):
    hostname = urlparse(url).hostname or url
    
    print('[*] Checking website...')
    time.sleep(0.5)
    
    for url in [f'http://{hostname}', f'https://{hostname}']:
        try:
            response = requests.get(url, timeout=5)
                
            if response.status_code == 200:
                print(f'{color.GREEN}[+] Site is up!{color.RESET}')
            else:
                print(f"[!] Website is up and responded with status {color.YELLOW}{response.status_code}{color.RESET}.")
                
            return True
        
        except requests.RequestException:
            continue

            
    print(f"{color.RED}[-] Website is offline.{color.RESET}")
    return False
    
def website_up(mode, host = None):
    if mode == 1:
        while True:
            url = input('[?] Enter the URL: ')
            
            if not url.startswith(("http://", "https://")):
                url = "https://" + url
                
            if(validate_url(url)):
                
                isUp(url)
                
                while True:
                    print('\n[1] Verify another website')
                    print('[0] Exit')
                    option = int(input('>> '))
                    if option == 1:
                        break
                    elif option == 0:
                        return 
                    else:
                        print(f'\n{color.YELLOW}[!] Invalid option{color.RESET}')
                        continue
            else:
                clear_terminal()
                print(f'\n{color.YELLOW}[!] Invalid URL{color.RESET}')
                continue
    elif mode == 2:
        if host != None:
            if not host.startswith(("http://", "https://")):
                host = "https://" + host
                
            return isUp(host)
        else:
            print(f'\n{color.RED}[-] Host not informed.{color.RESET}')
    
    else:
        print(f'\n{color.YELLOW}[!] Invalid mode{color.RESET}')
