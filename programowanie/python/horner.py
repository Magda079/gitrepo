#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  horner.py
#


def horner_it(stopien, tbwsp, x):
	wynik = tbwsp[0]
	for i in range(1, stopien + 1):
		wynik = wynik * x + tbwsp[i]

	return wynik


def main(args):
	tbwsp = []
	stopien = 3
	x = int(input("Podaj wartośc x: "))
	for i in range(0, 4):
		tmp = int(input("Podaj współczynniki: "))
		tbwsp.append(tmp)

	print("Wynik: ", horner_it(stopien, tbwsp, x))
	return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
