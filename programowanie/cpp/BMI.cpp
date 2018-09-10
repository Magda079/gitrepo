/*
 * BMI.cpp
 * 
 * 
 */


#include <iostream>
using namespace std; 

int main(int argc, char **argv)
{
	float masa;
    cout << "Podaj masę: ";
    cin >> masa; 

    float wzrost;
    cout << "Podaj wzrost: ";
    cin >> wzrost; 
    
    float bmi;
    bmi = masa/(wzrost*wzrost);
    
    cout << "BMI = " << bmi << endl;

    if(bmi < 18.5)
       {
         cout << "Niedowaga" << endl;
        }
        else if (bmi >= 18.5 && bmi < 25)
            cout << "Norma" << endl;
        else if (bmi>=25 && bmi < 30) 
            cout << "Nadwaga" <<endl;
        else if (bmi>=30) 
            cout << "Otyłość" << endl;
    
        
	return 0;
}

