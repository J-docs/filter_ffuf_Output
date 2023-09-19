#!/usr/bin/python3

import sys
import json

# creating function for processing file 
def filter_result(input_file):
    file = open(input_file,"+r")
    data = json.load(file)

    # printing header
    print('')
    print('--------------------------------------------------------------')
    print('[*] Command: '+data['commandline'])
    print('[*] Date & Time: ' +data['time'])

    # print('')
    print('--------------------------------------------------------------')
    print('INPUT			STATUS				URL')
    print('--------------------------------------------------------------')
    
    for i in data['results']:
	    print( '/' + str(i['input']['FUZZ']) + '			' + str(i['status']), ' 		'+ str(i['url']))

    file.close()

def jls_extract_def():
        #Checking file argument
        try:
            file = sys.argv[1]
        except IndexError:
            print("Usages: %s <file_name>" % sys.argv[0])
            print("Example: %s ffuf_result_file" % sys.argv[0])
            sys.exit(-1)
        return file

#main function
if __name__ == "__main__":

    #calling functions
    file = jls_extract_def()
    
    filter_result(file)