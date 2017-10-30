#!/usr/bin/env python
# -*- coding: utf-8 -*-

#osoba = "Adam Słodowy"
#osoba = 'Adam Słodowy' # zmiennych nie deklarujemy , cudzysłów jaki chcesz, ale nie mieszać
osoba = input('Jak się nazywasz?') # input pobiera dane
wiek = input ('Ile masz lat?') 
print('Witaj,', osoba, '!') # print wyprowadza 
print('Urodziłaś się w ', 2017 - int(wiek))
rok_pythona = 1991 
wiek_pyhona = 2017 - rok_pythona

if wiek_pyhona > int(wiek):
    print ('Jestem starszy!')
elif wiek_pyhona < int (wiek):
    print ('Jestem młodszy!')
else:
    print('Mamy tyle samo lat!')
