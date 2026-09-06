from services.port_up import port_up
from services.website_up import website_up
from services.full_check import full_check

import functions.colors as color
from functions.clear_terminal import clear_terminal


def vigil():
    print(r"""
____   ____.__       .__.__   
\   \ /   /|__| ____ |__|  |  
 \   Y   / |  |/ ___\|  |  |  
  \     /  |  / /_/  >  |  |__
   \___/   |__\___  /|__|____/
             /_____/           v1.0.0

[1] Check if the website is online.
[2] Check if the port is open.
[3] Full Check
[0] Exit
""")

while True:
    clear_terminal()
    vigil()
    try:
        option = int(input('>> '))

        if option == 1:
            clear_terminal()
            website_up(1)
        elif option == 2:
            clear_terminal()
            port_up()
        elif option == 3:
            full_check()
        elif option == 0:
            print(f"{color.GRAY}\n[*] Exiting...\n{color.RESET}")
            break
        else:
            continue
    
    except ValueError:
        continue
    
    except (KeyboardInterrupt, EOFError):
        print(f'{color.GRAY}\n\n[-] Interrupted by user.\n{color.RESET}')
        break
        
    
        