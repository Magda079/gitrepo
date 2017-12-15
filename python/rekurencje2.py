#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rekurencje2.py
#  
#  


def nwd_rek(a, b):
    if b == 0:
        return a
    return nwd_rek(b, a % b)

def main(args):
    
    a = int(input('Podaj liczbę naturalną'))
    b = int(input('Podaj liczbę naturalną '))

    print("NWD({:d}, {:d}) = {:d}".format(a, b, nwd_rek(a, b)))
    print('Największy wspolny dzielnik', nwd_rek(a, b))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
