#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sort_wybor_Lasota.py
#  
#  

import random


def wypelnij(liczby, ileliczb, maks):

    ile = 0  
    
    while ile < ileliczb:
        liczba = random.randint(0, maks)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            ile +=1

    return liczby


def sort_wybor(tab):
    
    print("------- Sortowanie przez wybieranie ------")
    for i in range(len(tab)):
        k = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[k]:
                k = j
        tab[i], tab[k] = tab[k], tab[i]
    return tab


def main(args):
    ile = 10
    tab = []
    maks = int(input('Podaj maksymalną liczbe: '))
    print(wypelnij(tab, ile, maks))
    print(sort_wybor(tab))
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
