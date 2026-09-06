import time
import socket
import requests
from urllib.parse import urlparse

import functions.colors as color
from functions.validate_url import validate_url
from functions.clear_terminal import clear_terminal

def isUp(host):
    hostname = urlparse(host).hostname or host

    for url in [f"http://{hostname}", f"https://{hostname}"]:
        try:
            start = time.perf_counter()
            response = requests.get(url, timeout=5)
            end = time.perf_counter()

            latency = end - start

            return True, response.status_code, latency

        except requests.RequestException:
            continue

    return False, None, None
    
    
def full_check():
    clear_terminal()
    while True:
        host = input('\n[?] Enter the host: ')
        
        if not host.startswith(("http://", "https://")):
            host = "https://" + host
            
        if(validate_url(host)):
            online, status_code, latency = isUp(host)
            ports = [443, 80, 8080]
            ports_status = []
            
            if(online):
                for port in ports:
                    try:
                        with socket.create_connection((urlparse(host).hostname, port), timeout=3):
                            ports_status.append("OPEN")

                    except ConnectionRefusedError:
                        ports_status.append("CLOSED")

                    except TimeoutError:
                        ports_status.append("FILTERED")

                    except OSError:
                        ports_status.append("ERROR")

                try:
                    ipv4 = socket.gethostbyname(urlparse(host).hostname)
                except socket.gaierror:
                    print("\n[-] Could not resolve hostname.")
                    continue
                
                print(f'\nFull Check - Result')
                print('────────────────────────────')

                print(f'{color.GREEN}[✓]{color.RESET} Site: {color.GRAY}{host}{color.RESET}')
                print(f'{color.GREEN}[✓]{color.RESET} IPV4: {color.GRAY}{ipv4}{color.RESET}')
                print(f'{color.GREEN}[✓]{color.RESET} Status: {color.GRAY}ONLINE{color.RESET}')
                print(f'{color.GREEN}[✓]{color.RESET} HTTP: {color.GRAY}{status_code}{color.RESET}')
                print(f'{color.GREEN}[✓]{color.RESET} Latência: {color.GRAY}{latency:.3f} s{color.RESET}')

                print(f'\nPorts')
                print('────────────────────────────')

                for port, status in zip(ports, ports_status):
                    print(f'[{status}] {color.GRAY}{port}{color.RESET}') 
                 
                 
                while True:
                    print('\n[1] Make Another Full Check')
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
                print(f'\n{color.RED}[-] Host is offline.{color.RESET}')
                continue
                
        else:
            print(f'\n{color.YELLOW}[!] Invalid URL{color.RESET}')
            continue