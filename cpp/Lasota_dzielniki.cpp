/*
 * Lasota_dzielniki.cpp
 * 
 */


#include <iostream>
using namespace std;

int main()
{
    int dzielna;
    
    cout << "Podaj wartosc: ";
    cin >> dzielna;
    
    cout << "Dzielniki liczby " << dzielna << " wynosza: ";
    
    for (int i = dzielna; i > 0; i--)
    {
        if (dzielna % i == 0)
            cout << dzielna / i << " ";
    
    }
    
    return 0;
}

