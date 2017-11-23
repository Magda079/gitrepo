/*
 * minmax.cpp
 */


#include <iostream>
using namespace std;


int main(int argc, char** argv) {
   
    int n;
    int tab[100];
 
   cout<<"Podaj liczbe n: ";
   cin>>n;
    
    for (int i=1;i<=n;i++)
    {
        tab[i]=i;
    }
  
    int min=tab[1];
    int max=tab[1];
    
    for(int i=1;i<=n;i++)
        {
        if(tab[i]<min)
            {
                min=tab[i];
            }

        if(tab[i]>max)
            {
                max=tab[i];
            }
        }
    
    cout<<"Wartosc minimalna to: "<<min<<endl;
    cout<<"Wartosc maksymalna to: "<<max<<endl;

    return 0;
}
