/*
 * euklides.cpp
 * 
 */


#include <iostream>

using namespace std;

int euklides_v1(int a, int b){
	//int a,b;
	while(a!=b)
	{
		if (a > b)
			a = a - b;
		else
			b = b - a;		
		}
		return a;
}

int euklides_v2(int a, int b){
    while(a>b)
    {
        a = a % b;
        b = b - a;
    }
    return b;
}

int main(int argc, char **argv)
{
	int a;
	int b;
	cout <<"Podaj pierwszą liczbę: "<<endl;
	cin >> a;
	cout<< "podaj drugą liczbę: "<<endl;
	cin >> b;
	cout<<"największy wspólny dzielnik: " << euklides_v1(a, b) << endl;

	return 0;
}
