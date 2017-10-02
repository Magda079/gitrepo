/*
 * kolo.cpp
 * 
 * Copyright 2017  <>
 
 * 
 */


#include <iostream>
#include <math.h>
using namespace std;
int main(int argc, char **argv)

{
	int r = 0;
    cout << "Podaj promień: ";
    cin >> r;
    cout << "Pole " << M_PI*r*r << endl;
    cout << "Obwód " << 2*M_PI*r << endl;
    
	return 0;
}

