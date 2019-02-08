# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 20:31:25 2019

@author: admin
"""

import sys
import re


def Words(filename):
    

    #filename = 'Alice.txt'
    file = open(filename, 'rb')
    raw = file.read()
    raw = raw.decode('utf-8')

    
    #remove the punctuations
    replaced = re.sub("[^a-zA-Z' ]+", '', raw)
    #split the txt into words
    raw=replaced.split()
    
    #remove duplicates
    mylist = list(dict.fromkeys(raw))
    #sort words
    mylist=sorted(mylist)
    
    for item in mylist:
        sys.stdout.write(item + '\n')
        
        
def main():
    
    if len(sys.argv) == 2:
        filename=sys.argv[1]
        Words(filename)
    else:
        raw = sys.stdin.readline()
        Words(raw)
        
    
    
    
if __name__=='__main__':
    main() 