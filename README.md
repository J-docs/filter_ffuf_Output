# filter_ffuf_Output
[+] Description:
This repository contains a small Python script  which will help you to refine or filter the output file of ffuf tool.

[+] what it does:
when you run ffuf tool for directory busting and and save the output in file with -o flag.

Example: ffuf -u http://localhost/FUZZ -w /usr/share/wordlists/dirb/common.txt -o ffuf2.txt

[+] How tO use:
  python3 filter_fuff.py <file_name>


*There may be simpler ways to do the same thing, but I found this to be the best way to learn Python.*
