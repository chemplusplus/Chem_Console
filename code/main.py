import requests

import json

import sys

TITLE = '''

   _____ _                               
  / ____| |                    _     _   
 | |    | |__   ___ _ __ ___ _| |_ _| |_ 
 | |    | '_ \ / _ \ '_ ` _ \_   _|_   _|
 | |____| | | |  __/ | | | | ||_|   |_|  
  \_____|_| |_|\___|_| |_| |_|           
                                         
                                         
'''

print(TITLE)

TABLE = dict()
   
if sys.platform == 'linux':
	temp = json.load(open("assets/ptable.json", "r"))["Table"]["Row"]

elif sys.platform == 'win32':
	temp = json.load(open("assets\\ptable.json", "r"))["Table"]["Row"]
   
for i in temp:
	TABLE[i['Cell'][2]] = i['Cell']
