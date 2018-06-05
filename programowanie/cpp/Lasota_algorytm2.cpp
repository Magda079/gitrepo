/*
 * algorytm2.cp
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int n;
    cin >> n; 
 

    int suma = 0;
    int ile_parzystych;
 
    for(int i=0; i<n; i++)
    {
        int liczba; 
        cin >> liczba;
     
        if(liczba % 2 == 0) 
            {
                suma += liczba;
                ile_parzystych++;
            }
    }
 
    cout << "Parzyste: " << ile_parzystych << "\nSuma: " << suma << endl;
	
	return 0;
}

