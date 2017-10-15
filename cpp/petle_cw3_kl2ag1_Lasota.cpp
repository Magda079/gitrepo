/*
 * petle_cw3_kl2ag1_Lasota.cpp
 * 
 */


#include <iostream>

using namespace std;
int main(int argc, char **argv)
{
	int x = 0;
    
    cout << "Podaj liczbę: " << endl; 
    
    do  
        {
          cin >> x; 
        }
        while ((x < 0) || (x > 15)) ;
        
	return 0;
}


