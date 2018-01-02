#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sort_wybor_Lasota.py
#  
#  

from random import randint


def wypelnij(tab, n, m):
    ile = 0
    while ile < n:
        liczba = randint(0, m)
        if tab.count(liczba) == 0:
            tab.append(liczba)
            ile += 1
    return tab


def sort_wyb(tab, n):
    for i in range(0, n):
        k = i
        j = i + 1
        for j in range(j, n + 1):
            if tab[j] < tab[k]:
                k = j
        tab[j], tab[k] = tab[k], tab[j]
    return tab




def main(args):
    ile = 10
    tab = [ile]
    max = int(input("Maksymalna liczba do tabeli: "))
    print("Tabela: ", wypelnij(tab, ile, max))
    print("Sortowanie poprzez wybieranie : ", sort_wyb(tab, ile))

    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
