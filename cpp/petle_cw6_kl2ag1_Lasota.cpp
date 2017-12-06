/*
 * petle_cw6_kl2ag1_Lasota.cpp
 */


#include <cstdlib>
#include <iostream>

using namespace std;

void dziel (int licznik, int dzielnik){
    int a,b,c,d;
    
    a = licznik;
    b = dzielnik;
    
    c=0;
    d=a;
    
    while (d>=c){
        c = c + 1;
        d = d-b;
        
        }
    cout << "Wynik dzielenia: " << c << endl;
    cout << "Reszta: " << d << endl; 
    }

int main (int argc, char **argv)
    {
        int a = 0;
        int b = 0;
        cout << "Podaj licznik: " ;
        cin >> a;
        cout << "Podaj mianownik: ";
        cin >> b;
        if (a == 0){
            cout << "Licznik nie może być zerem";
            } else 
            dziel(a,b);
        
        return 0;
        }
