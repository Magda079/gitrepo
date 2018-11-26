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
    
    kl3A = Klasa(nazwa='3A', roknaboru=2010, rokmatury=2013)
    kl3A.save() #zapisanie obiektu w bazie 
    kl1A = Klasa(nazwa='1A', roknaboru=2009, rokmatury=2012)
    kl1A.save()
    
    u1 = Uczen(imie='Michał', nazwisko='Wołodyjowski', plec=False, klasa=kl3A)
    u1.save()
    u2 = Uczen(imie='Anna', nazwisko='Gacek', plec=True, klasa=kl1A)
    u2.save()
    u3 = Uczen(imie='Jan', nazwisko='Zioło', plec=False, klasa=kl1A)
    u3.save()
    
    #zapytania czyli kwerendy w orm
    uczniowie = Uczen.select()
    for u in uczniowie:
        print(u.id, u.nazwisko, u.klasa.nazwa)
        
    klasy = Klasa.select()
    for k in klasy:
        for u in k.uczniowie:
            print(u.nazwisko)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
