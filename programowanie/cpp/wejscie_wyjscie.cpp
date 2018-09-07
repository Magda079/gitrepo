/*
 * imie.cpp
 *
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{   
    char imie[10];
    cout << "Podaj imię: ";
    cin >> imie;
	
    cout << "Cześć, " << imie << "!" << endl; 
    
    int a,b;
    char dzialanie;
    cout << "Działanie?";
    cin >>dzialanie;
    cout << "Liczba a: "; cin >> a;
    cout << "Liczba b: "; cin >> b;
    
    if (dzialanie == '+' )
      cout << a + b << endl;
    else if (dzialanie == '-' )
      cout << a - b << endl;
    
	return 0;
}

