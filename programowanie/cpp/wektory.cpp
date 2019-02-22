/*
 * wektory.cpp 
 * 
 */


#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;


struct punkt{
    int x;
    int y;
};

struct wektor{
    punkt pp;
    punkt pk; 
};

punkt wylicz_srodek(wektor w){
    punkt ps;
    ps.x = ((float)(w.pp.x + w.pk.x)/2);
    ps.y = ((float)(w.pp.y + w.pk.y)/2);
    return ps;
}

wektor getWektor(){
    wektor wl;
    cout << "Podaj współrzędne punktu początkowego: \n";
    cin >> wl.pp.x;
    cin >> wl.pk.y;
    cout << "Podaj współrzędne punktu końcowego: \n";
    cin >> wl.pp.x;
    cin >> wl.pk.y;
    return wektor;
}


int main(int argc, char **argv)
{
    wektor wl = getWektor;
    punkt ps = wylicz_srodek(wl);
    cout << "Współrzędne wektora o punktach: \n";
	return 0;
}

