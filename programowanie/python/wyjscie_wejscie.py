#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wyjscie_wejscie.py
#  


def main(args):
    
    osoba = input('Jak się nazywasz?')
    print('Witaj,', osoba, '!')
    
    dzialnie = input ("Działanie? ")
    
    if dzialanie == "+":
        print(a + b)
    elif dzialanie == "-":
        print(a - b)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
