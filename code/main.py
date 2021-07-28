import requests

import json

import sys

import os

import string

def clear_screen():
	if sys.platform == "linux":
		os.system("clear")
	elif sys.platform == 'win32':
		os.system('cls')
clear_screen()

TITLE = '''
   _____ _                               
  / ____| |                    _     _   
 | |    | |__   ___ _ __ ___ _| |_ _| |_ 
 | |    | '_ \ / _ \ '_ ` _ \_   _|_   _|
 | |____| | | |  __/ | | | | ||_|   |_|  
  \_____|_| |_|\___|_| |_| |_|           
                                         
Welcom to Chem++ Console Version 
Type Help for a list of Commands
'''

THINGS = [
        "AtomicNumber",
        "Symbol",
        "Name",
        "AtomicMass",
        "CPKHexColor",
        "ElectronConfiguration",
        "Electronegativity",
        "AtomicRadius",
        "IonizationEnergy",
        "ElectronAffinity",
        "OxidationStates",
        "StandardState",
        "MeltingPoint",
        "BoilingPoint",
        "Density",
        "GroupBlock",
        "YearDiscovered"
      ]


print(TITLE)

TABLE = dict()
   
if sys.platform == 'linux':
	temp = json.load(open("assets/ptable.json", "r"))["Table"]["Row"]

elif sys.platform == 'win32':
	temp = json.load(open("assets\\ptable.json", "r"))["Table"]["Row"]
   
for i in temp:
	TABLE[i['Cell'][2]] = i['Cell']
	
def info(x):
	print(f"\n\t+---Info on {x}---")
	for e in TABLE:
		if x == e:
			for i in range(len(TABLE[e])):

				if TABLE[e][i] == '':
					print(f"\t|{i} = Unknown")

				else:
					print(f"\t|{THINGS[i]} = {TABLE[e][i]}")
	print("\t+-----------" + "-"*len(x) + "---\n")

def command(x):
	global RUNNING
	if x == "Exit":

		RUNNING = False

	elif x == "Help":
		to_print = '''
Help: Displays list of Commands

Exit: Exits Chem++'''

		print(to_print)

	elif x[:4] == "Info":
		info(x[5:])

	elif x == "Cls" or x == 'cls':
		clear_screen()


RUNNING = True

while RUNNING:
	print("```", end = '')
	
	CMD = str(input(""))
	
	command(CMD)
	
	
	
print("\nExiting Chem++")

clear_screen()
	
	
	
