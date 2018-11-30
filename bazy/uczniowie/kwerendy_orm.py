#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py

from uczniowie_model import * 

def kw01(): 
    query = Uczen.select().where(Uczen.imie.startswith('G')) # dolowna zmienna , ta wybiera wszystkich uczniów z klasy 
    for obj in query:
        print(obj.nazwisko, obj.imie, obj.egz_hum)

def main(args):
    baza.connect()
    
    kw01()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
