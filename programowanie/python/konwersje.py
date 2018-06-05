#!/usr/bin/env python
# -*- coding: utf-8 -*-


def konwersja1(liczba10, podsatwa):
    """
    funkcja zmienia liczbe dziesietna na system o podanej podstawie
    """
    liczba = []  # lista reszty
    while liczba10 != 0:
        reszta = lista10 % podstawa  # obliczanie reszty z dzielenia
    if reszta > 9:
        reszta = chr(reszta + 55)
        liczba.append(str(reszta))
        liczba10 = int(liczba10 / podstawa)
    liczba.reverse()  #odwrócenie klejności elementów!!
    return"".join(liczba)  # złączenie elementów listy w jeden ciąg teksu

def dec2other():
    """
    funkcja pobiera liczbe i podstawe od uzytkownika
    """
    liczba = int(input("podaj liczbe: "))
    liczba = int(input("podaj podstawe: "))
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("podaj podstawe:"))
    print("wynik konwersji: {}(10) = {} ({}) ". format(
        liczba, konwersja1(liczba, podstawa), podstawa))


def konwersja2(liczba,podstawa):
    """funkcja konwertuje liczbe w system o podanej podstawie na system
    dziesietny"""
    liczba10 = 0
    potega = len(liczba) - 1
    for cyfra in liczba:
        if not cyfra.isdigit():
            liczba10 += ord(cyfra.upper()) - 55 * (podstawa ** potega)
        else:
            liczba10 += int(cyfra) * (podstawa ** potega)
        potega -= 1
    return liczba10


def other2dec():

    podstawa = int(input("podaj podsatwe:"))
    liczba = int(input("podaj liczbę:"))
    for i in liczba:
        if i.isdigit():
            cyfra = int(i)
        else:
            cyfra = ord(i.upper()) - 55
        if cyfra > podstawa - 1:
            print ("podales nie dopuszczalna liczbe!"



def main(args):
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
def main(args):
    print("Zamiana liczby dziesiętnej na liczbę o podanej podstawie:"
          "<2;16> lub odwrotnie.")
    dec2other()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
