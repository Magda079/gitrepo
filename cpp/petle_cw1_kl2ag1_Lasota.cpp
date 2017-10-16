/*
 * cwiczenie1.cpp
 */


#include <iostream>
#include <math.h>

using namespace std;
int main(int argc, char **argv)
{
    int i=0;
    
        for (;;)
        {
            cout << "Podaj liczbę : ";
            cin >> i;
            cout << "Kwadrat liczby: " << i*i << endl;
            cout << "Pierwiastek: " << sqrt(i) << endl;
            if (i>0)
            break;
            
        }
    
	return 0;
}
