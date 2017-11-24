#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minmax.py
#  

import random

def losuj(ileliczb, maksliczb):
    liczby = []  # zbiór pusty

    ile = 0
    # for i in range(ileliczb):
    while ile < ileliczb:
        liczba = random.randint(0, maksliczb)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            ile += 1
    #  print(lista)
    return liczby
    
def minimum(lista):
    #  wyszukiwanie minimum
    min = lista[0]
    #  for i, el in enumerate(lista):
    for el in lista:
        if el < min :
            min = el
    return min
    
def maksimum(lista):
    max = lista[0]
    for i, el in enumerate(lista):
        if el > max:
            max = el
    return max
        
def main(args):
    lista = losuj(10, 50)
    assert minimum ([7,5,2,1,2]) == 1
    assert maksimum ([7,5,2,1,2]) == 7
    print("Min: ", minimum(lista))
    print("Max: ", maksimum(lista))
    print(lista)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
