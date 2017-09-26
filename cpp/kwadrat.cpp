/*
 * hello.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    
    int bok = 0 ; //deklaracja i inicjacja zmiennej 
    
    cout << "Podaj bok: " << endl;
    
	cin >> bok;
    cout << "Obwód " << 4 * bok << endl 
         << "Pole: " << bok * bok << endl; 
        
    
	return 0;
}

