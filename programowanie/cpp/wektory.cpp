/*
 * wektory.cpp 
 * 
 */


#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

#define ILE 2

struct punkt{
    int x;
    int y;
}

struct wektor{
    punkt pp;
    punkt pk; 
}

void drukuj(punkt []){
    for(int i=0; i < ILE; i++){
        cout << "Punkt: " << endl;
        cout << setw(10) << left << "X: "; cout << tb[i].x << endl; 
        cout << setw(10) << left << "Y: "; cout << tb[i].y << endl;
        }    
}

int main(int argc, char **argv)
{

        
	return 0;
}

