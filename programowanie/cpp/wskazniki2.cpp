/*
 * wskazniki2.cpp
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int roz = 20;
	int tab[roz]; // nazwa tablicy jest wskaźnikiem
    int *wsk1; // zmienna wskaźnikowa
    wsk1 = tab;
    cout << tab << endl;
    cout << wsk1 << endl;

    *wsk1 = 10;
    cout << tab[0] << endl;
    wsk1++;
    *wsk1 = 12;

	return 0;
}

