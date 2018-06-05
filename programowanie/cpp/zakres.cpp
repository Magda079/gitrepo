/*
 * funkcje.cpp
 */


#include <iostream>

using namespace std; 

//int liczba,krok; // zmienne globalne 
int zwieksz(int liczba, int krok) { //przekazywanie parametru przez wartość dostaje kopie
    liczba = liczba + krok; // zmienne są lokalne dla tej funkcji
    krok = 3* krok;
    return krok; 
}

void zwieksz2(int &a, int &b) { //& specjalny operator dzięki niemu dostaje dostęp do oryginałów
    a = a + b;
    b = 3*b;
    
}

int main(int argc, char **argv)
{
    int liczba,krok; // zmienne lokalne 
    cout << "Podaj liczbę i krok: " ;
    cin >> liczba >> krok;
    
    cout << "Liczba: " << liczba << " "<< &liczba << endl;
    
    //zwieksz2(liczba, krok);
    //cout << "Liczba i krok: " << liczba << " " << krok << endl;
    
	return 0;
}

