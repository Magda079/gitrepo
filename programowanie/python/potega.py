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


#  potega_rek (a, 0) = 1 dla a różnego od 0
#  potega_rek(a, n) = potega_rek(n - 1) * a dla n = N+

def potega_rek(a, n):
    if n == 0:
        return 1
    return potega_rek(n - 1) * a


def main(args):
    a = int(input('Podaj podstawę '))
    b = int(input('Podaj wykładnik '))

#  while b < 0:
#  wynik = a ** b

    print (a ** b)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
