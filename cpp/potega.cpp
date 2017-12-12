/*
 * potega.cpp
 * 
 * Copyright 2017  <>
 * 
 */
#include <iostream>

using namespace std;

float potega_it(float x, int n)
{
    float wynik = 1;
    for (int i = 1; i <= n; i++)
    {
        wynik = wynik * x;
    }
    return wynik;
}

int potega_rek(int x, int n)
{    
    if (x == 0)
        return 0;
    else if (n == 0)
        return 1;
    return potega_rek(x, n - 1) * x;
}

int main(int argc, char **argv)
{
    int n;
    float x;
    cout << "Podaj podstawe potęgi: " << endl;
    cin >> x;
    cout << "Podaj wykładnik potęgi: " << endl;
    cin >> n;
    cout << "Potęga: " << potega_rek(x, n) <<endl;
	return 0;
}
