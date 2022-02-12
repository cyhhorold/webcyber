import os
import pyfiglet
import platform as pf
from colorama import Fore, init
import time

init()

sys = pf.uname()[0]

if sys == 'Linux':
    os.system('clear')


banner = pyfiglet.figlet_format('NMAP ATTACKS')

print(banner)

print(Fore.LIGHTYELLOW_EX+'''Script BY : DRCYBER

Team Builder : Eagle-Root

Relationship : -https://zil.ink/drcayber- ''')

print('')

print(Fore.GREEN+'                                |- Type of Attack -| \n')

time.sleep(1)

print(Fore.LIGHTYELLOW_EX+' [1] Xss bug site \n')
time.sleep(0.09)
print(Fore.LIGHTYELLOW_EX+' [2] User wordperes \n')
time.sleep(0.09)
print(Fore.LIGHTYELLOW_EX+' [3] Port Scan -65535- \n')
time.sleep(0.09)
print(Fore.LIGHTYELLOW_EX+' [4] Attacks King \n')
time.sleep(0.09)
print(Fore.LIGHTYELLOW_EX+' [5] IP Fwd \n')
time.sleep(0.09)
print(Fore.LIGHTYELLOW_EX+' [6] Wordpress enum \n')
time.sleep(0.09)
print(Fore.LIGHTYELLOW_EX+' [7] Wordpress brute \n')
time.sleep(0.09)
print(Fore.LIGHTYELLOW_EX+' [8] Bug sql injection \n')
time.sleep(0.09)
print(Fore.LIGHTYELLOW_EX+' [9] Dns brute \n')
time.sleep(0.09)
print(Fore.LIGHTYELLOW_EX+' [10] Site Map \n')
time.sleep(0.09)
print(Fore.LIGHTBLUE_EX+' [99] Exit :) \n')



number_select = input(Fore.CYAN+'Select Number [1 , 10] : ')

print('')

if number_select == '1':

    ip = input(Fore.GREEN+' Enter the IP/domin : ')
    print('')

    os.system('nmap --script=http-xssed '+str(ip))

elif number_select == '2':

    ip = input(Fore.GREEN+' Enter the IP/domin : ')

    print('')

    os.system('nmap --script=http-wordpress-users '+str(ip))

elif number_select == '3':

    ip = input(Fore.GREEN+' Enter the IP/domin : ')
    print('')
    os.system('nmap -p- '+str(ip))



elif number_select == '4':

    ip = input(Fore.GREEN+' Enter the IP/domin : ')
    print('')

    os.system('nmap -A -O -sS -V -v -S -sn -oA -Pn '+str(ip))



elif number_select == '5':

    ip = input(Fore.GREEN+' Enter the IP/domin : ')
    print('')

    os.system('nmap --script=ip-forwarding '+str(ip))



elif number_select == '6':

    ip = input(Fore.GREEN+' Enter the IP/domin : ')
    print('')

    os.system('nmap --script=http-wordpress-enum '+str(ip))



elif number_select == '7':

    ip = input(Fore.GREEN+' Enter the IP/domin : ')
    print('')

    os.system('nmap --script=http-wordpress-brute '+str(ip))




elif number_select == '8':

    ip = input(Fore.GREEN+' Enter the IP/domin : ')
    print('')

    os.system('nmap --script=http-sql-injection '+str(ip))



elif number_select == '9':

    ip = input(Fore.GREEN+' Enter the IP/domin : ')
    print('')

    os.system('nmap --script=dns-brute '+str(ip))



elif number_select == '10':

    ip = input(Fore.GREEN+' Enter the IP/domin : ')
    print('')

    os.system('nmap --script=http-sitemap-generator '+str(ip))

elif number_select == '99':
    os.system('python3 webcyber.py')

