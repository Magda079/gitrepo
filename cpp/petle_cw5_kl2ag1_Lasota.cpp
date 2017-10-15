/*
 * petle_cw5_kl2ag1_Lasota.cpp
 */

#include <cstdlib>
#include <iostream>

using namespace std;
int main(int argc, char **argv)
{
    int liczba;
    cout << "Podaj liczbę: " ;
    cin >> liczba;
    do 
    {
        int suma =0;
        int lic = liczba;
        while (lic > 0) {suma += lic%10; lic/=10;};
        liczba=suma;
        cout << "Suma wynosi" << liczba << endl;
    }while (liczba>9);
    cout << "Ostatnia suma cyfr wynosi: " << liczba << endl;
   
    system ("pause");
	
	return 0;
}

