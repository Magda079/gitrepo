#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
import sqlite3

def kwerenda1(cur):
    cur.execute("""
    WITH srednie AS (
       SELECT nazwisko, AVG(ocena), klasa AS srednia FROM uczniowie
       INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
       INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
       GROUP BY uczniowie.id
    """)
    
        # ~WITH srednie AS (
            # ~SELECT imie, nazwisko, AVG(ocena) AS srednia FROM uczniowie
            # ~INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
            # ~GROUP BY id_uczen
        # ~) SELECT imie, nazwisko, srednia FROM srednie
          # ~WHERE srednia > 3.8 
        # SELECT wybierz WITH z tabeli -->> () wybierz ... z srednie
        # nie można stosować GROUP BY i WHERE razem 
        # ~ORDER BY srednia DESC
        # ~LIMIT 10  
        # limit 10 - najlepsi z 10 wyników  DESC malejące ASC rosnące 
        # ~SELECT imie, nazwisko, COUNT(ocena) AS ilu FROM oceny
        # ~INNER JOIN uczniowie ON oceny.id=uczniowie.id_klasa
        # ~GROUP BY ocena
        # ~ORDER BY ilu DESC
    #        ORDER BY klasa ASC - sortowanie rekordów

     # ~SELECT nazwisko, imie1, dzien, miesiac, rok FROM nazwiska
        # ~INNER JOIN dane_osobowe 
        # ~ON nazwiska.nr_ucznia=dane_osobowe.nr_ucznia
        # ~WHERE nazwiska.nr_ucznia=9201
    #        SELECT * FROM nazwiska WHERE nazwisko LIKE 'G%'
    wyniki = cur.fetchall() #pobranie wszystkich rekordów na raz
    for row in wyniki:
        print(tuple(row))


def main(args):
    ### KONFIGURACJA ###
    baza_nazwa = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    roz = '.csv'
    naglowki = True
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
