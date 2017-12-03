#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  horner.py
#  


def horner(k, tbwsp, x):
    wynik = tbwsp[i]
    for i in range(1, k):
        wynik = wynik * x + tbwsp[0]
        print("Wynik: ")

def main(args):
    
    for i in range(0,4):
        tbwsp = int(input("Podaj wartość współczynnika: "))
        x = float(input("Podaj x: "))
        k = 3
        print(horner)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
