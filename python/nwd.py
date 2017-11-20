#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nwd.py
#  
#  znaleźć największy wspólny dzielnik swóch liczb naturalnych całkowitych ,
#  która znajdzie za pomoca pętli NWD... euklidesa klasyczny oparty na odejmowaniu

def nwd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
        return a 

def main(args):
    
    a=int(input('Podaj liczbę '))
    b=int(input('Podaj liczbę '))
    
    print ('Największy wspolny dzielnik', nwd(a,b) )
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
