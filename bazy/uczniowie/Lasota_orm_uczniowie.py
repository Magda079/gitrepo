#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py
#  

import os
from uczniowie_model import * 

def czy_jest(plik):
    if not os.path.isfile(plik):
        print("Plik {} nie istnieje!".format(plik))
        return False
    return True
    
def czytaj_dane(plik, separator=","):
    dane = []  # pusta lista na rekordy
    
    if not czy_jest(plik):
        return dane
    
    with open(plik, newline='', encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=separator, skipinitialspace=True)
        for rekord in tresc:
            dane.append(rekord)
    
    return dane
    
def dodaj_dane(dane):
    for model, plik in dane.items():
        print(model._meta.fields)
        
def main(args):
    
    if os.path.exists(baza_nazwa):
        os.remove(baza_nazwa)
    baza.connect()  # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Przedmiot, Ocena])   #mapowanie ORM (odwzorować)
    
    dane = {
        Klasa: 'klasy',
        Uczen: 'uczniowie',
        Przedmiot: 'przedmioty',
        Ocena: 'oceny'
    
    }
    
    
    dodaj_dane(dane)
    
    baza.commit()
    baza.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
