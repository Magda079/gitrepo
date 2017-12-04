#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  py1.py
#  


def algorytm(n,a): 
    iloczyn = 1
    i = 1
    while i = 1 : 
        if i = n :
            iloczyn = iloczyn*a
        else:
            i = i + 1
        return iloczyn
            
        
    return iloczyn 
    

def main(args):
    n = int(input("Podaj n: "))
    a = int(input("Podaj a: "))
    
    print("Iloczyn: ", algorytm(n,a))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
