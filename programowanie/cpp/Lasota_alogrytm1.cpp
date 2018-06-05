/*
 * alogrytm1.cpp
 * 
 * Copyright 2017  <>
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int n,a ;
    int iloczyn = 1;
    int i =1;
    cout << "Podaj  n: " << endl;
    cin >> n ;
    while (i != n)
    {
            cout << "Podaj a: " << endl;
            cin >> a;
            iloczyn = iloczyn*a ;
            i++;
        
    } 
    cout << "Wynik: " << iloczyn << endl;
	
	return 0;
}

