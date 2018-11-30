#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py

from uczniowie_model import * 

def kw01(): 
    # query = Uczen.select().where(Uczen.imie.startswith('G')) # dolowna zmienna , ta wybiera wszystkich uczniów z klasy 
    # query = Uczen.select().where(Uczen.imie == 'Rafał')
    # query = Uczen.select().where(Uczen.imie == 'Rafał').count()
    # print(query)
    query = (Uczen
        .select()
        .where(Uczen.egz_mat.between(30,35))
        .order_by(Uczen.egz_mat.asc())) # asc - rosnąco | desc - malejąco 
    for obj in query:
        print(obj.nazwisko, obj.imie, obj.egz_mat)

def kw02():
    query = (Uczen
        .select(Uczen.nazwisko, Uczen.klasa.klasa)
        .join(Klasa)
        .order_by(Uczen.klasa.klasa))
    for obj in query:
        print(obj.nazwisko, obj.klasa.klasa)
    
def main(args):
    baza.connect()
    
    kw02()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
