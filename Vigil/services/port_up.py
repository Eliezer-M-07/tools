import socket

import functions.colors as color
from services.website_up import website_up
from functions.clear_terminal import clear_terminal

def port_up():
    while True:
        clear_terminal()
        host = input('\n[?] Enter the host: ')

        if website_up(2, host):
            port = int(input('[?] Enter the port: '))

            try:
                with socket.create_connection((host, port), timeout=3):
                    print(f'\n{color.GREEN}[+] The port {port} is open.{color.RESET}')
            except (TimeoutError, ConnectionRefusedError, OSError):
                print(f'\n{color.GRAY}[-] The port {port} is not open.{color.RESET}')
                
            while True:
                print('\n[1] Verify another port')
                print('[0] Exit')
                
                option = int(input('>> '))
                
                if option == 1:
                    break
                elif option == 0:
                    return
                else:
                    print(f'\n{color.GRAY}[!] Invalid option{color.RESET}')
                    continue
        else:
            continue