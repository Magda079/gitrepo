/*
 * Lasota_ulamek.cpp
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int a;
    int b;
    cout << "Podaj licznik a: " << endl;
    cin >> a;
    cout << "Podaj mianownik b: " << endl;
    cin >> b;
    int licznik = a;
    int mianownik = b;
    
    if( a != b ) {
       
        do {
            if( a > b ) {
                a = a - b;
            }
            if( a < b ) {
                b = b - a;
            };
        }
        while ( a != b );
       
    }
    
   
    licznik = licznik / a;
    mianownik = mianownik / a;
    cout <<"Skrócony ułamek: "<< licznik << "/" << mianownik << endl;
    
    
	return 0;
}
