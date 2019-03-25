/*
 * osoba.cpp
 * 
 */
#include <iostream>
#include <cstdlib>
#include "osoba.h"

Osoba::Osoba(){
        ;
}

Osoba::Osoba(string i, string n, int w, bool p){
    imie = i;
    nazwisko = n;
    wiek = w;
    plec = p;
}

void Osoba::laduj() {
    cout << "Dodaj osobę:" << endl;
    cout << "Imię: "; cin >> imie;
    cout << "Nazwisko: "; cin >> nazwisko;
    cout << "Wiek: "; cin >> wiek;
    cout << "Płeć: "; cin >> plec;
}

void Osoba::dane() {
    cout << endl;
    cout << "Twoje dane:" << endl;
    cout << "Imię: " << imie << endl;
    cout << "Nazwisko: " << nazwisko << endl;
    cout << "Wiek: " << wiek << endl;
    cout << "Płeć: " << plec << endl;
}
