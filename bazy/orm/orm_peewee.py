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
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
   
        
class Uczen(KlasaBaza):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    
        
class Wynik(KlasaBaza):
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='wyniki')
    
        
def main(args):
    
    if os.path.exists(baza_nazwa):
        os.remove(baza_nazwa)
    baza.connect()  # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])   #mapowanie ORM (odwzorować)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
