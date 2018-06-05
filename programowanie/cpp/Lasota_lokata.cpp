/*
 * Lasota_lokata.cpp
 */


#include <iostream>

using namespace std;

int main()
{
    int suma, ile, wplata;
    wplata = 100;
    suma = 0;
    int i;
    
    cout << "Wprowadz ilosc wplat: ";
    cin >> ile;
    
    for(i =0; i<ile; i++) 
    {
    suma = wplata + suma;
    wplata = 10 + wplata;

    }
    
    cout << "Ostatnia kwota wpłaty: " << wplata-10 << endl;
    cout << "Stan konta: " << suma << endl;
    
    return 0;
}

