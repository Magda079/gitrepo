#include <iostream>
#include <cmath>
using namespace std;

float st, rad;

int main()
{
	st = 0.0;
	cout << cos(90 * M_PI/180);
	//cin >> rad;
	return 0;
    do
	{
		rad = st*M_PI/180;
		cout << "cos(" << st << ") = " << cos(rad) << endl;
		st+=10.0;
	}
	//while(st != 90);
	while(cos(rad)!=0.0);
    return 0;
}

