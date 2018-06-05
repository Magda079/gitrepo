/*
 * rekurencje3.cpp
 * 
 */

#include <iostream>

using namespace std;

int kwadrat (int n)
{
    if (n <= 0) 
        return 0;
    return kwadrat(n-1) + 2*n - 1;
}


int main(int argc, char **argv)
{
    int n;
    cout << "Podaj liczbę: ";
    cin >> n;
    cout << "Wynik: " << kwadrat(n) << endl;
    
    return 0;
}


