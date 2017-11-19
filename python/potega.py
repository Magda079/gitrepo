#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#  

def potega(a,b):
    wynik = 1
    while b > 0:
        wynik = a ** b
    return wynik


def main(args):
    a=int(input('Podaj podstawę '))
    b=int(input('Podaj wykładnik '))
    
    assert type (a) == int
    assert type (b) == int 
    
    #while b < 0:
        #wynik = a ** b 
   
    assert potega (0) == 0
    assert potega (1) == 1
    assert potega (2) == 4
    assert potega (3) == 9
        
    print ( a ** b )
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
