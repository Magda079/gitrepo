/*
 * formatowanie.cpp
 * 
 */


#include <iostream>
#include <iomanip>
#include <cstdio> // printf
#include <cmath> // stała M_PI
#include <bitset>

using namespace std; 

int main(int argc, char **argv)
{
	int liczba = 255;
    float lrz = 12.786;
    
    cout.fill('-');
    cout << setw(10) << liczba << endl;
    cout << setw(10) << lrz << endl; 
    
    cout << setw(10) << hex << showbase << uppercase << liczba << endl;
    cout << setw(10) << oct << showbase << uppercase << liczba << endl;
    cout << bitset<8>(liczba) << endl;
    
    // char tb[20];
    // cin.getline(tb, 20);
    // for(int i=1, i < 20, i++ ) cout << tb[i];
    // int i=0;while tb[] != '\0' { cout << tb[i]; i++;}
    string tekst;
    cin >> ws >> tekst;
    cout << tekst << endl;
    
    cout.precision(4);
    cout << setw(10) << lrz << endl; 
    
    printf("Liczba Pi: %12.3f\n", 10*M_PI); // szerokosc - 12
    printf("Hex: %#x\nOct: %#o", liczba, liczba);
        
	return 0;
}

