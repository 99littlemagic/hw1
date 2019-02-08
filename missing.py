# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 20:18:02 2019

@author: admin
"""

import sys

from argparse import ArgumentParser


def main():
    
    p = ArgumentParser(description='transfer input')
    
    try:
        p.add_argument('integer', type = int, default = None)
    except:   
        pass 
    
    p.add_argument('string',type=str)
    args = p.parse_args()
    N = args.integer
    number= args.string   
    # Get number_list
    number_list = [int(i) for i in number.strip(' ').split(' ')]
    
    if isinstance(N, int)==True:
        n=len(number_list)
        if all( type(i) is int for i in number_list ):      
                if len(number_list) != N-1:
                    print("Error: The number of items provided in the second argument does not match N-1")
                
                elif len(set(number_list)) < len(number_list):
                     print("Error: There are duplicate values in the second argument")
                     
                else:
                    n=len(number_list)
                    total = (n+1)*(n+2)/2
                    sum_of_A = sum(number_list)
                    miss=total - sum_of_A 
                    print('The missing number is: '+str(miss))
                    
                    
                     
        else:
             print("Error: A non-integer value is provided in the second argument.")
             
         
       
        
        
if __name__ == '__main__':
    main()
