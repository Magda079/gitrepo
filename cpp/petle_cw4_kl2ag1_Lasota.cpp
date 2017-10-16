/*
 * petle_cw4_kl2ag1_Lasota.cpp
 */

#include <cstdlib>
#include <iostream>
using namespace std;
int main()
{
  int n;
  cout << "Podaj liczbe calkowita";
  cin  >> n;
  int  lic=abs(n);  
        
  int s=0;    
  while(lic > 0)  
      { 
        s += lic % 10; 
        lic /= 10;  
       }
       
    cout << "Suma cyfr liczby " << n << "wynosi" << s << endl;
    system("PAUSE");
return 0;
}
        
        
	

