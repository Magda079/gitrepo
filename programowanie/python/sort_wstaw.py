#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sort_wstaw.py
#

from math import floor
from random import random


def sort_wst(lista):
    for i in range(1, len(lista)):
        el = lista[i]
        k = i - 1
        while k >= 0 and lista[k] > el:
            lista[k + 1] = lista[k]
            k -= 1
        lista[k + 1] = el
    return lista


def szukaj_bin(lewy, prawy, lista, el):
    """Wersja liniowa wyszukiwania binarnego,
    wyszukujemy indeks do wstawienia elementu """
    while lewy < prawy:
        srodek = floor((lewy + prawy) / 2)
        if el <= lista[srodek]:
            prawy = srodek
        else:
            lewy = srodek + 1
    return lewy


def sort_wst_bin(lista):
    for i in range(1, len(lista)):
        el = lista[i]
        # wyszuk. bin. indeksu do wstawiania el
        k = szukaj_bin(0, i, lista, el)
        lista = lista[:k] + [el] + lista[k:i] + lista[i + 1:]
        print (lista)
    return lista

def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9]
    print(lista)
    print(sort_wst_bin(lista))
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
