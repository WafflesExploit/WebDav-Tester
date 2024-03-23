 # HTTPMethodChecker
 ### -> Checks if the specified HTTP methods are allowed for each URL present in the provided wordlist.
 ### -> Usage example: Finding URLs with the PUT method to upload malicious files.
## Table of Contents
* [Installation](#installation)
* [Example Usage](#Example-Usage)
* [Usage](#Usage)
* [Contact](#contact)

## Installation
 ```
 $ git clone https://github.com/WafflesExploits/HTTPMethodChecker
 ```

## Example Usage
```
$ python ./HTTPMethodChecker.py -w urltest.txt -m 'PUT,OPTIONS,POST' -o output.txt
* Starting HTTP Method Checker at 2023-11-21 16:32:44.
| 
| Settings:
| Wordlist: urltest.txt | HTTP Methods: PUT,OPTIONS,POST
|
| Credits:
| By (https://github.com/WafflesExploits)
|
| Results: 
| URL: http://example.com/ 
| - HTTP Methods found:  OPTIONS, POST
| URL: http://www.itsecgames.com/  
| - HTTP Methods found:  POST, OPTIONS
| 
| Results have been outputted to: output.txt.
|
* Finished scan in 0.849s.
```

## Usage
```
./HTTPMethodChecker.py -h                    
usage: HTTPMethodChecker.py [-h] [-w WORDLIST] [-m [METHODS]] [-o [OUTPUT]]

-> Checks if the specified HTTP methods are allowed for each URL present in the provided wordlist.
-> Usage example: Finding URLs with the PUT method to upload malicious files.

options:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        Wordlist containing the URLs to scan.
  -m [METHODS], --methods [METHODS]
                        Specifies the HTTP methods to search for. Default: 'PUT,DELETE,COPY,MOVE,SEARCH,PROPFIND'
  -o [OUTPUT], --output [OUTPUT]
                        Outputs results to a file.
```

## Contact
Created by [@WafflesExploit](https://github.com/WafflesExploit) - feel free to contact me!

