// osoba.h
#include <iostream>
#include <cstdlib>

#ifndef __OSOBA_H_
#define __OSOBA_H_

using namespace std;

class Osoba {
    private:
        string imie;
        string nazwisko;
        int wiek;
        bool plec;
        
    public:
        Osoba();  // konstruktor
        Osoba(string, string, int, bool); // konstruktor

};
#endif
