import pyfiglet
import time
import whois
import colorama
import platform as pl
import os


def start():


    sysclear = pl.uname()[0]

    if sysclear == 'Linux':
        os.system('clear')

    elif sysclear == 'Windows':
        os.system('cls')


    banner = pyfiglet.figlet_format('WHOIS')

    print(banner)
    print(colorama.Fore.LIGHTYELLOW_EX+'''    Script BY : DRCYBER

    Team Builder : Eagle-Root

    Relationship : -https://zil.ink/drcayber- ''')


    print('')


    domin_name = input(colorama.Fore.LIGHTGREEN_EX+'[!] domin Name : '.capitalize()).casefold()


    info_saved = whois.whois(domin_name)

    time.sleep(1)

    print('')
    print(colorama.Fore.LIGHTYELLOW_EX+'~ domin Info ~'.capitalize())
    print('')
    print(info_saved)

    reloading = input('Exit as Script ? (Y / N) ').casefold()
    if reloading == 'n':
        os.system('python3 webcyber.py')
        
    else:
        reloading == 'y'
        exit()



start()