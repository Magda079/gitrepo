#!/usr/bin/env python
# -*- coding: utf-    szyfrogram = ""


def szyfruj_cezar(tekst, klucz):
    klucz = klucz % 26
    szyfrogram = ""
    for znak in tekst:
        znak = znak.upper()  # .lower też może być
        ascii = ord(znak) + klucz  # kod ascii litery zastępującej
        if ascii > 90:
            ascii - 26
        szyfrogram += chr(ord(znak) + klucz)
    return szyfrogram


def deszyfruj(szyfrogram, klucz):
    tekst = ""
    for znak in szyfrogram:
        ascii = ord(znak) - klucz
        if ord(znak) == 32:
            ascii = 32
        if ascii > 90 and ascii < 97:
            ascii -= 26
        elif ascii > 122:
            ascii -= 26
        tekst += chr(ascii)
    return tekst


# obsłużyc spacje
# obsłużyć male i duże litery


def main(args):
    tekst = input("Podaj tekst :")
    klucz = int(input("Klucz: "))

    szyfrogram = szyfruj_cezar(tekst, klucz)
    print(szyfrogram)
    print(deszyfruj(szyfrogram, klucz))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
