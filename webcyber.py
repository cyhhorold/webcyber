from time import sleep
from colorama import Fore, init
import platform as pf
import os
import pyfiglet

sysinfo = pf.uname()[0]

if sysinfo == 'Linux':

    os.system('clear')

banner = pyfiglet.figlet_format('WEBCYBER')

print(banner)


print('')

sleep(1)

print(Fore.YELLOW+' Script By : DRCYBER\n\n Team cybery : Eagle-ROOT\n\n links : https://zil.ink/drcayber\n')

print(Fore.LIGHTRED_EX+'[1] SCANNER WEB\n\n[2] INFO-DOMIN\n\n[3] PANEL ADMIN\n\n[4] DDOS Attacks\n\n[5] Wordpress Brute Force\n\n[6] Attacks Sqlinjection\n\n')

select = input(Fore.LIGHTBLUE_EX+'Select Number [1 , 6] : ').casefold()

if select == '1':
    os.system('python3 scanner.py')
elif select == '2':
    os.system('python3 domin.py')
elif select == '3':
    os.system('python2 admin_panel.py')
elif select == '4':
    os.system('python3 dos.py')
elif select == '5':
    os.system('python3 wordpressB.py')
elif select == '6':
    os.system('python3 sqldata.py')
