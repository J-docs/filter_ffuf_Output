# filter_ffuf_Output
[+] Description:
      This repository contains a small Python script  which will help you to refine or filter the output file of ffuf tool.

[+] what it does:
   when you run ffuf tool for directory busting and and save the output in file with -o flag
     example: ffuf -u http://192.168.188.14/FUZZ -w /usr/share/wordlists/dirb/common.txt -o ffuf2.txt
  
[+] This is how it looks inside output file (fuff1.txt) looks like:
  
{"commandline":"ffuf -u http://192.168.188.14/FUZZ -w /usr/share/wordlists/dirb/common.txt -o ffuf2.txt","time":"2023-09-07T23:49:17+05:30","results":[{"input":{"FFUFHASH":"91dcbc","FUZZ":".htaccess"},"position":12,"status":403,"length":279,"words":20,"lines":10,"content-type":"text/html; charset=iso-8859-1","redirectlocation":"","scraper":{},"duration":139045243,"resultfile":"","url":"http://192.168.188.14/.htaccess","host":"192.168.188.14"},{"input":{"FFUFHASH":"91dcbb","FUZZ":".hta"},"position":11,"status":403,"length":279,"words":20,"lines":10,"content-type":"text/html; charset=iso-8859-1","redirectlocation":"","scraper":{},"duration":139176538,"resultfile":"","url":"http://192.168.188.14/.hta","host":"192.168.188.14"},{"input":{"FFUFHASH":"91dcbd","FUZZ":".htpasswd"},"position":13,"status":403,"length":279,"words":20,"lines":10,"content-type":"text/html; charset=iso-8859-1","redirectlocation":"","scraper":{},"duration":142878146,"resultfile":"","url":"http://192.168.188.14/.htpasswd","host":"192.168.188.14"},{"input":{"FFUFHASH":"91dcb1","FUZZ":""},"position":1,"status":200,"length":10701,"words":3427,"lines":369,"content-type":"text/html","redirectlocation":"","scraper":{},"duration":139698125,"resultfile":"","url":"http://192.168.188.14/","host":"192.168.188.14"},{"input":{"FFUFHASH":"91dcb7e4","FUZZ":"index.html"},"position":2020,"status":200,"length":10701,"words":3427,"lines":369,"content-type":"text/html","redirectlocation":"","scraper":{},"duration":136679145,"resultfile":"","url":"http://192.168.188.14/index.html","host":"192.168.188.14"},{"input":{"FFUFHASH":"91dcb861","FUZZ":"javascript"},"position":2145,"status":301,"length":321,"words":20,"lines":10,"content-type":"text/html; charset=iso-8859-1","redirectlocation":"http://192.168.188.14/javascript/","scraper":{},"duration":138079156,"resultfile":"","url":"http://192.168.188.14/javascript","host":"192.168.188.14"},{"input":{"FFUFHASH":"91dcb989","FUZZ":"manual"},"position":2441,"status":301,"length":317,"words":20,"lines":10,"content-type":"text/html; charset=iso-8859-1","redirectlocation":"http://192.168.188.14/manual/","scraper":{},"duration":136117852,"resultfile":"","url":"http://192.168.188.14/manual","host":"192.168.188.14"},{"input":{"FFUFHASH":"91dcbd6c","FUZZ":"robots.txt"},"position":3436,"status":200,"length":59,"words":11,"lines":2,"content-type":"text/html","redirectlocation":"","scraper":{},"duration":136491170,"resultfile":"","url":"http://192.168.188.14/robots.txt","host":"192.168.188.14"},{"input":{"FFUFHASH":"91dcbe04","FUZZ":"server-status"},"position":3588,"status":403,"length":279,"words":20,"lines":10,"content-type":"text/html; charset=iso-8859-1","redirectlocation":"","scraper":{},"duration":138611945,"resultfile":"","url":"http://192.168.188.14/server-status","host":"192.168.188.14"}],"config":{"autocalibration":false,"autocalibration_keyword":"FUZZ","autocalibration_perhost":false,"autocalibration_strategy":"basic","autocalibration_strings":[],"colors":false,"cmdline":"ffuf -u http://192.168.188.14/FUZZ -w /usr/share/wordlists/dirb/common.txt -o ffuf2.txt","configfile":"","postdata":"","debuglog":"","delay":{"value":"0.00"},"dirsearch_compatibility":false,"extensions":[],"fmode":"or","follow_redirects":false,"headers":{},"ignorebody":false,"ignore_wordlist_comments":false,"inputmode":"clusterbomb","cmd_inputnum":100,"inputproviders":[{"name":"wordlist","keyword":"FUZZ","value":"/usr/share/wordlists/dirb/common.txt","template":""}],"inputshell":"","json":false,"matchers":{"IsCalibrated":false,"Mutex":{},"Matchers":{"status":{"value":"200,204,301,302,307,401,403,405,500"}},"Filters":{},"PerDomainFilters":{}},"mmode":"or","maxtime":0,"maxtime_job":0,"method":"GET","noninteractive":false,"outputdirectory":"","outputfile":"ffuf2.txt","outputformat":"json","OutputSkipEmptyFile":false,"proxyurl":"","quiet":false,"rate":0,"recursion":false,"recursion_depth":0,"recursion_strategy":"default","replayproxyurl":"","requestfile":"","requestproto":"https","scraperfile":"","scrapers":"all","sni":"","stop_403":false,"stop_all":false,"stop_errors":false,"threads":40,"timeout":10,"url":"http://192.168.188.14/FUZZ","verbose":false,"wordlists":["/usr/share/wordlists/dirb/common.txt"],"http2":false}}                                                                                                                                                          


-> This script prints the above file into very simple output like this:    
--------------------------------------------------------------
[*] Command: ffuf -u http://192.168.188.14/FUZZ -w /usr/share/wordlists/dirb/common.txt -o ffuf2.txt
[*] Date & Time: 2023-09-07T23:49:17+05:30
--------------------------------------------------------------
INPUT			STATUS				URL
--------------------------------------------------------------
/.htaccess			403  		http://192.168.188.14/.htaccess
/.hta			    403  		http://192.168.188.14/.hta
/.htpasswd			403  		http://192.168.188.14/.htpasswd
/			        200  		http://192.168.188.14/
/index.html			200  		http://192.168.188.14/index.html
/javascript			301  		http://192.168.188.14/javascript
/manual			    301  		http://192.168.188.14/manual
/robots.txt			200  		http://192.168.188.14/robots.txt
/server-status		403  		http://192.168.188.14/server-status
                                                                                        

[+] How tO use:
      # python3 filter_fuff.py <file_name>

[+] There may be simpler ways to do the same thing, but I found this to be the best way to learn Python.
