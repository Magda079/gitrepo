#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
#  
#  Copyright 2018  <>
#  

import sqlite3

def kwerenda1(cur):
    cur.execute("""
        SELECT klasa, nazwisko, imie FROM klasy
        INNER JOIN uczniowie
        ON klasy.id=uczniowie.id_klasa
    """)
    
    #  SELECT * FROM nazwiska WHERE nazwisko LIKE 'G%'
    wyniki = cur.fetchall() 
    for row in wyniki:
        print(tuple(row))

         #WHERE nazwiska.nr_ucznia=
        #(SELECT nr_ucznia FROM nazwiska
        #WHERE nazwisko='German' AND imie1='Dariusz') #oceny

        #SELECT nazwisko, imie1, dzien, miesiac, rok FROM nazwiska
        #INNER JOIN dane_osobowe 
        #ON nazwiska.nr_ucznia=dane_osobowe.nr_ucznia
        #WHERE nazwiska.nr_ucznia=9201
        
        #SELECT nazwisko, imie1, dzien, miesiac, rok FROM nazwiska
        #INNER JOIN dane_osobowe 
        #ON nazwiska.nr_ucznia=dane_osobowe.nr_ucznia
        #WHERE nazwiska.nr_ucznia=
        #(SELECT nr_ucznia FROM nazwiska
        #WHERE nazwisko='Gryczon' AND imie1='Agata')


def main(args):
    ### KONFIGURACJA ###
    baza_nazwa = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    roz = '.csv'
    naglowki = False
    ####################
    
    con = sqlite3.connect(baza_nazwa + '.db')
    cur = con.cursor()  # obiekt tzw. kursora
   
    kwerenda1(cur)
   

    con.commit()
    con.close()
    return 0 
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
