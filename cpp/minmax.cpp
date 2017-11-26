/*
 * minmax.cpp
 */




#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;
int main()
{
    srand( time( NULL ) );
    int tab[ 6 ];
    int x;
    int min, max;
 
    cout << "Wylosowane liczby: " << endl << endl;
    for( int i = 0; i < 6; i++ )
    {
        do
        {
            x =( rand() % 49 ) + 1;
        }
        while(( tab[ 0 ] == x )||( tab[ 1 ] == x )||( tab[ 2 ] == x )||( tab[ 3 ] == x )||( tab[ 4 ] == x )||( tab[ 5 ] == x ) );
 
        tab[ i ] = x;
 
        cout << tab[ i ] << " ";
    }
 
     min = tab[0];
 
    for(int i=0; i<6; i++)
    {
        if(min>tab[i])
        {
            min = tab[i];
        }
    }
 
    max = tab[0];
 
    for(int i=0; i<6; i++)
    {
        if(max<tab[i])
        {
            max = tab[i];
        }
    }
    cout<<endl;
    cout<<"najmniejsza liczba to: "<<min<<endl;
    cout<<"najwieksza liczba to: "<<max<<endl;
    return 0;
}
 
