# filter_ffuf_Output
[+] Description:
This repository contains a small Python script  which will help you to refine or filter the output file of ffuf tool.

[+] what it does:
When you use the ffuf tool and save the results in a file using the -o flag, the output file can be messy when it's in JSON format. This script takes the messy output file as input and then prints the information in a much simpler and easier-to-read format. 

Example: ffuf -u http://localhost/FUZZ -w /usr/share/wordlists/dirb/common.txt -o ffuf2.txt

[+] How tO use:
  python3 filter_fuff.py <file_name>
  ex: python3 filter_fuff.py ffuf2.txt


*There may be simpler ways to do the same thing, but I found this to be the best way to learn Python.*
