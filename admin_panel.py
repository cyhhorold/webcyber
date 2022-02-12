from urllib2 import Request, urlopen, URLError, HTTPError
from colorama import Fore, init
import os
import platform as pf

sysclear = pf.uname()[0]

if sysclear == 'Linux':
    	os.system('clear')

init()

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input(Fore.GREEN+"Enter Site Name : ")
	print Fore.LIGHTBLUE_EX+"\n\nPanel links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print Fore.YELLOW+"OK => ",req_link
os.system('figlet ADMIN PANEL')
print(Fore.LIGHTYELLOW_EX+'''Script BY : DRCYBER

Team Builder : Eagle-Root

Relationship : -https://zil.ink/drcayber- \n''')

findAdmin()