/*
 * horner.cpp
 */


#include <iostream>

using namespace std; 

//W(x) = 2x^3 + 3x^2 + 5x + 4 
//W(x) = x (2x^2 + 3x+ 5) + 4
//W(x) = x (x (2x + 3) + 5) + 4  

float horner_it(int k, float tbwsp[], float x){
        int i;
        float wynik = tbwsp[0];
        for (i= 1; i < k + 1; i++){
            wynik = wynik * x + tbwsp[i];
            }
        return wynik;
    }

int horner_rek(int k, float tbwsp[], float x)

    if ()
        return;
    else
        return horner_rek


int main(int argc, char **argv)
{
	int stopien = 3;
    float x;
    float tbwsp[4];
    int i=0;
    
    cout << "Podaj wartość x " << endl;
    cin >> x; 
    
    
    for (i = 0; i < 4; i++) {
        cout << "Podaj współczynnik: ";
        cin >> tbwsp[i];
    }
    cout << horner_it(stopien, tbwsp, x) << endl; 
    
    //tbwsp[4] = wartość
	return 0;
}

