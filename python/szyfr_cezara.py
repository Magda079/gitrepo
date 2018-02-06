#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj_cezar(tekst, klucz):
    klucz = klucz % 26
    szyfrogram = ""
    for znak in tekst:
        znak = znak.upper()  # .lower też może być

        szyfrogram += chr(ord(znak) + klucz)
    return szyfrogram

def main(args):
    tekst = input("Podaj tekst :")
    klucz = int(input("Klucz: "))

    szyfrogram = szyfruj_cezar(tekst, klucz)
    print(szyfrogram)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
