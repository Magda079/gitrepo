/*
 * pliki.cpp
 */


#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <iomanip>

using namespace std;

void zmienNazwe1(char t1[], char t2[]) {
    // kopiowanie znaków z tablicy do tablicy
    // METODA 1
    // tekst.txt
    int i=0;
    while(t1[i] != '.') {
        t2[i] = t1[i];
        i++;
    }
    t2[i]='.';
    t2[++i]='b';
    t2[++i]='a';
    t2[++i]='k';
    t2[++i]='\0';

}

void zmienNazwe2(char t1[], char t2[]) {
    // kopiowanie znaków z tablicy do tablicy
    // METODA 2
    // tekst.txt
    char *wsk;
    strcpy(t2, t1);
    wsk = strstr(t2, ".txt");
    strncpy(wsk, ".bak", 4);
}

int liczZnaki(char nazwa[]) {
    char kopia[15];
    zmienNazwe2(nazwa, kopia);
    cout << kopia << endl;
    
    // otwieranie pliku
    ifstream wejscie(nazwa);
    if (!wejscie) { cout << "Brak pliku!"; return 1; }
    
    ofstream wyjscie(kopia);
    if (!wyjscie) { cout << "Błąd pliku!"; return 1; }
    
    char znak;
    int ile, ileal; //, ilenum, ilealnum
    ile = ileal = 0; //= ilenum = ilealnum 

    while(!wejscie.eof()) {
        wejscie.get(znak); // odczytanie poj. znaku
        if (wejscie) ile++;
        if (wejscie && isalpha(znak)) ileal++;  // liczymy litery
        //if (wejscie && isdigit(znak)) ilenum++;  // liczymy cyfry
        //if (wejscie && isalnum(znak)) {
            //ilealnum++;  // liczymy litery i cyfry
            //wyjscie.put(znak); // zapisanie znaku do pliku
        //}
        if ((int)znak == 10)
            wyjscie.put('\n');
    }
    wejscie.close(); wyjscie.close();
    cout << "Znaków: " << ile << endl;
    cout << "Liter: " << ileal << endl;
    //cout << "Cyfr: " << ilenum << endl;
    return ile;
}

// odczytaj z pliku tekst.txt liczby, w tym rzeczywiste,
// i zapisz je w pliku cyfry.txt
// 

int zapiszSamogloski(char nazwa[]) {
    char kopia[15] = {"samogloski.txt"};
    // otwieranie pliku
    ifstream wejscie(nazwa);
    if (!wejscie) { cout << "Brak pliku!"; return 1; }
    ofstream wyjscie(kopia);
    if (!wyjscie) { cout << "Błąd pliku!"; return 1; }
    
    char znak;
    while(!wejscie.eof()) {
        wejscie.get(znak); // odczytanie poj. znaku
        if ( (wejscie && isalpha(znak)) || znak == '.') {
            wyjscie.put(znak);
        }
        if ((int)znak == 10)
            wyjscie.put('\n');
    }
    wejscie.close(); wyjscie.close();
    return 0;
}

void sumuj(char nazwa[]){
    ifstream wejscie(nazwa);
    float liczba;
    float suma=0;
    while(!wejscie.eof()) {
        wejscie >> liczba;
        suma += liczba;
    };
    cout << "Suma: " << suma << endl;
}

int main(int argc, char **argv)
{
    char nazwa[15];
    cout << "Podaj nazwę pliku: ";
    cin.getline(nazwa, 15);
    cout << nazwa << endl;
    liczZnaki(nazwa);
    zapiszSamogloski(nazwa);
    sumuj(nazwa);
    return 0;
}
