#!/usr/bin/env python3
# Created by https://github.com/WafflesExploits
import subprocess
import re
import sys
import argparse
import time
from time import sleep
from datetime import datetime

parser = argparse.ArgumentParser(description='-> Checks if the specified HTTP methods are allowed for each URL present in the provided wordlist. \n -> Usage example: Finding URLs with the PUT method to upload malicious files.')
parser.add_argument('-w', '--wordlist', type=str, help="Wordlist containing the URLs to scan.")
parser.add_argument('-m', '--methods', type=str, nargs='?', default='PUT,DELETE,COPY,MOVE,SEARCH,PROPFIND',help="Specifies the HTTP methods to search for. Default: 'PUT,DELETE,COPY,MOVE,SEARCH,PROPFIND'")
parser.add_argument('-o', '--output', type=str, nargs='?',help="Outputs results to a file.")
NumberOfArgs = len(sys.argv)

if(NumberOfArgs<=2): # If there is only one argument or less, prints out the Script's Usage.
	parser.print_help()
	sys.exit()

args = parser.parse_args()

Wordlist = args.wordlist
Methods = args.methods
Output = args.output



MethodsArray = Methods.split(",") # Splits the string from the methods arg to an array Ex: 'PUT,OPTIONS,POST' -> ['PUT', 'OPTIONS', 'POST']
MethodJoined = ('|'.join(MethodsArray)).replace("'", "") # Remove -> '
MethodsRegex = f"({MethodJoined})" # (PUT|OPTIONS|POST)

URLWordlist = []
with open(f'{Wordlist}') as f: # Opens and automatically closes the passwordfile.
    lines = f.readlines()
    for urls in lines:
	    URLWordlist.append(urls.replace('\n', "")) # Removes \n from the URLs and appends them to URLWordlist

def cmd(cmdstr):
	try:
		strlist = cmdstr.split() # Splits the command into a list ["host", "-t", "mx",...]
		return (subprocess.check_output(strlist, stderr=subprocess.STDOUT).decode('utf-8')) # Executes the cmd and returns output
	except Exception as error:
		print(error)

def RegexFinder(pattern, data): # Matches text from data based on regex pattern.
	return re.finditer(pattern, data)





# Start of the execution

currentDate = str(datetime.now())
StartTime = time.time()
print(f"* Starting HTTP Method Checker at {currentDate[:-6]}");
print("| ")
print("| Settings:")
print(f"| Wordlist: {Wordlist} | HTTP Methods: {Methods}")
print("|")
print("| Credits:")
print("| By (https://github.com/WafflesExploits)")

NumberOfMatches = 0
print("|")
print("| Results: ")
file = open(Output, "w+")
for URLs in URLWordlist:
	data = cmd(f"curl -X OPTIONS {URLs} -i") # Runs the curl command for every URL in the URLWordlist
	
	Method_Matches = RegexFinder(MethodsRegex, data) # (PUT|OPTIONS|POST)
	
	
	methodus = [] # Create an empty list to store the matched HTTP methods
	for match in Method_Matches:
		methodus.append(match.group())
	if (len(methodus) > 0): 
		NumberOfMatches+=1
		print(f"| URL: {URLs} ")
		print(f"| - HTTP Methods found: ", end=" ")
		MethodsList = (", ".join(methodus))
		print(MethodsList) # Use the join() method to concatenate the methods with a comma separator
		if (Output is not None): 
			file.write(f"{URLs} - {MethodsList}\n")

file.close()
			
				

			
	
if (NumberOfMatches == 0):
	print("| - No Methods were found -")
else:
	print("| ")
	print(f"| Results have been outputted to: {Output}.")

print("|")
EndTime = time.time()
RunTime = EndTime - StartTime
print(f"* Finished scan in {str(RunTime)[0:5]}s.")

