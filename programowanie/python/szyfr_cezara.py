#!/usr/bin/env python
# -*- coding: utf-    szyfrogram = ""


def szyfruj_cezar(tekst, klucz):

    klucz = klucz % 26
    szyfrogram = ""
    for znak in tekst:
        #  znak = znak.upper()  # lower zmniejsza liczbę
        if ord(znak) > 64 and ord(znak) < 91:
            ascii = ord(znak) + klucz  # kod ascii litery zastępującej
            if ascii > 90:
                ascii -= 26
        if ord(znak) > 96 and ord(znak) < 123:
            ascii = ord(znak) + klucz
            if ascii > 122:
                ascii -= 26
        if ord(znak) == 32:
            ascii = 32
        szyfrogram += chr(ascii)
    return szyfrogram

def deszyfruj(szyfrogram, klucz):

    tekst = ""
    for znak in szyfrogram:
        #  tekst = tekst.upper()
        if ord(znak) > 64 and ord(znak) < 91:
            ascii = ord(znak) - klucz 
            if ascii > 90:
                ascii -= 26
        if ord(znak) > 96 and ord(znak) < 123:
            ascii = ord(znak) - klucz 
            if ascii >122:
                ascii -= 26
        if ord(znak) == 32:
            if ascii == 32:
                ascii = 32
            tekst += chr(ascii)
    
    return tekst # w pętli zastanów się co zwraca , z jakim kodem mamy do czynienia itp
  # obsłuż spacje oraz małe i duże litery

def main(args):

    tekst = input("Podaj tekst: ")
    klucz = int(input("Klucz: "))

    szyfrogram = szyfruj_cezar(tekst, klucz)
    print(szyfrogram)
    print(deszyfruj(szyfrogram, klucz))
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
