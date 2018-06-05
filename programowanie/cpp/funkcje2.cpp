/*
 * funkcje.cpp
 */


#include <iostream>

using namespace std; 
//definiowanie funkcji między int a using
 int sumuj(int a, int b) //funkcja - zawsze nawiasy , void nie zwraca wyniku ,int - zwraca wynik, jest zawsze return
{
    return a + b;
}

int odejmij(int a, int b) 
{
    return a - b;
}

int mnozenie(int a, int b) 
{
    return a * b;
}

int dzielenie(int a, int b) 
{
    return a / b; 
}

int main(int argc, char **argv)
{
	int a , b ;
    cout << "Podaj liczby: " ;
    cin >> a >> b;
    
    int suma = sumuj (a,b);
    int roznica = odejmij (a,b);
    int iloczyn = mnozenie (a,b);
    int iloraz = dzielenie (a,b);
    
    
    cout << "Suma: " << suma << endl;
    
    cout << "Różnica: " << roznica << endl;
    
    cout << "Iloczyn: "<< iloczyn << endl;
    
    cout << "Iloraz: " << iloraz << endl;
    
    
	return 0;
}

