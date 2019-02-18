/*
 * struktury.cpp
 */

#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

#define ILE 2

struct osoba{
    char imie[10];
    char nazwisko[20];
    int wiek= 0;
    
}; 

void drukuj(osoba tb[]){
    for(int i=0; i < ILE; i++){
        cout << "Dane ucznia: " << endl;
        cout << setw(11) << left << "Imię: "; cout << tb[i].imie << endl; 
        cout << setw(10) << left << "Nazwisko: "; cout << tb[i].nazwisko << endl;
        cout << setw(10) << left << "Wiek: "; cout << tb[i].wiek << endl;
        }    
}
 
void getOsoby(osoba tb[]){
    osoba o;
    for(int i=0; i < ILE; i++){
        cout << "Wprowadz dane ucznia: " << endl;
        cout << setw(11) << left << "Imię: "; cin >> o.imie; 
        cout << setw(10) << left << "Nazwisko: "; cin >> o.nazwisko;
        cout << setw(10) << left << "Wiek: "; cin >> o.wiek;
        cout<< endl; 
        tb[i] = o;
        }    
}

void zapiszOsoby(osoba tb[]){
    ofstream plik;
    plik.open("osoby.txt");
   for(int i=0; i < ILE; i++){
        plik << tb[i].imie << endl; 
        plik << tb[i].nazwisko << endl;
        plik << tb[i].wiek << endl;
    }     
    plik.close();
}
 
int main(int argc, char **argv) {
    
    osoba tb[ILE];
    getOsoby(tb);
    drukuj(tb);
    zapiszOsoby(tb);

	return 0;
}

