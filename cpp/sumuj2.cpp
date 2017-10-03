/*
 * sumuj.cpp
 * Program pobiera liczby od uzytkownika aż ich suma przekroczy 100.
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)


{
    //int i;
    int suma = 0;
    int liczba = 0;
    int ilosc = 0;
    cout << "Wyprowadzaj kolejne liczby" << endl;
    //for (;;)
    while (1) //pętla nieskończona
       {
        
        cin >> liczba;
        ilosc++;
        cout << "Podano: " << liczba << endl;
        suma += liczba;
        if (suma > 100)
           break;
       };
       cout << "Wprowadzono liczb: " << ilosc << endl;
       cout << "Suma liczb: " << suma << endl;
       
return 0;

}
