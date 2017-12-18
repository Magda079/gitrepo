/*
 * sort_wybor.cpp
 * 
 */


#include <iostream>

using namespace std; 

void wypelnij(int t[], int n, int maks){
    srand(time(NULL)); // inicjacja generatora liczb pseudolosowych
    for (int i = 0; i < n; i++){
        t[i] = 1 + rand() % maks; // losowanie liczb całkowitych <0,maks>
        
    }
    
}

void drukuj(int t[], int n){
        for (int i = 0; i < n; i++){
        cout << t[i] << " ";
    }
    cout << endl; 
    
}

int main(int argc, char **argv)
{
	const int ile = 10;
    int tab[ile];
    wypelnij(tab,ile,20);
    drukuj(tab,ile);
	return 0;
}

