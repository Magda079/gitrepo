#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py
#  

import os
from peewee import *


baza_nazwa = 'test.db'
baza = SqliteDatabase(baza_nazwa)  # instancja bazy

### MODELE #
class KlasaBaza(Model):
    class Meta:
        database = baza


class Klasa(KlasaBaza):
    klasa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)

class Uczen(KlasaBaza):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    klasa = ForeignKeyField(Klasa)
   
            
class Przedmiot(KlasaBaza):
    przedmiot = CharField(null=False)
    imie_naucz = CharField(null=False)
    nazwisko_naucz = CharField(null=False)
    plec_naucz = BooleanField()
    
    
class Ocena(KlasaBaza):
    datad = DateField(null=False)
    ocena = FloatField(default=0)
    przedmiot = ForeignKeyField(Przedmiot, related_name='oceny')
    przedmiot = ForeignKeyField(Uczen, related_name='oceny')
    
        
def main(args):
    
    if os.path.exists(baza_nazwa):
        os.remove(baza_nazwa)
    baza.connect()  # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Przedmiot, Ocena])   #mapowanie ORM (odwzorować)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
