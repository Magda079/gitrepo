/*
 * wskazniki.cpp
 * 
 */

#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int x = 13;
    double y = 10;
    int *wsk1; // zmienna wskaźnikowa
    double *wsk2;
    wsk1 = &x; // inicjacia wskaźnika
    wsk2 = &y;
    cout << x << endl;
    cout << wsk1 << endl;
    cout << &x << endl; 

    *wsk1 += 1;
    cout << *wsk1 << endl;

    wsk1 +=1;
    cout << wsk1 << endl;

    cout << sizeof(x) << endl;
    cout << sizeof(y) << endl;
    cout << wsk2 << endl;
    wsk2 += 1;


	return 0;
}


