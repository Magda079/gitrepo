/*
 * nwd.cpp
 */


#include <iostream>

using namespace std;

int nwd(int a,int b){
   if(a==b) return a;
   else 
      if(a>b)
        return nwd(a-b, b);
      else 
         return nwd(b-a, a);
}


int main(){

   int a,b;
   cout << "Podaj a ";
   cin >> a;
   cout << "Podaj b ";
   cin >> b; 
   
   cout << "Największy wspólny dzielnik: " << nwd(a,b) << endl;

return 0;
}
