/*
 * funkcje.cpp
 */


#include <iostream>

using namespace std; 
//definiowanie funkcji między int a using
 void sumuj(int a, int b) //funkcja - zawsze nawiasy
{
    cout << "Suma: " << a + b << endl;
}


void odejmij(int a, int b) 
{
    cout << "Różnica: " << a - b << endl;
}

void mnozenie(int a, int b) 
{
    cout << "Iloczyn: " << a * b << endl;
}

void dzielenie(int a, int b) 
{
    if ()
    cout << "Iloraz: " << a / b << endl;
    
    cout << "Nie dziel przez 0! " << endl; 
}

int main(int argc, char **argv)
{
	int a , b ;
    cout << "Podaj liczby: " ;
    cin >> a >> b;
    
    sumuj(a, b);
    
    odejmij (a, b);
    
    mnozenie (a, b);
    
    dzielenie (a, b);
    
    
	return 0;
}

