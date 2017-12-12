/*
 * fibonacci.cpp
 *
 */


#include<iostream>
#include<cstdlib>
using namespace std;
 
void fibonacci(int n)
{    
     int a = 0;
     int b = 0;
 
     for(int i=0;i<n;i++)
     {
            cout<<b<<" ";
            b += a; //pod zmienną b przypisujemy wyraz następny czyli a+b
            a = b-a; //pod zmienną a przypisujemy wartość zmiennej b
     }     
}
int fib_rek(int n)
{
    if (n < 2)
        return 1;
    else
        return fib_rek(n - 1) + fib_rek(n - 2);
    
}
 
int main()
{
    int n;
 
    cout<<"Podaj ile chcesz wypisać wyrazów ciągu fibonacciego: ";
    cin>>n;
 
    fibonacci(n);
    fib_rek(n);
    return 0;
}


