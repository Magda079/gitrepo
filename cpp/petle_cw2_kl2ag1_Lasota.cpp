/*
 * petle_cw2_kl2ag1_Lasota.cpp
 */


#include <iostream>
#include <cmath>

using namespace std;
int main(int argc, char **argv)
{
	int a,b,c;
    int n = 0;
    float p = 0;
    a = b = c = 0;
    
    for (;;)
    {
            cout << "Podaj boki: " ;
            cin >> a >> b >> c;
            
            if (a+b > c && a+c > b && b + c > a)
            {
                n = (a + b + c)/2;
                p = sqrt (n*(n-a)*(n-b)*(n-c)) ;
                cout <<"Pole trójkąta : " << p << endl;
                break;
            }
        
    } 
    
	return 0;
}

