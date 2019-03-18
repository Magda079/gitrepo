/*
 * samochod.cpp
 */

#include <iostream>
#include <cstdlib>
#include "car.h"

using namespace std;

int main(int argc, char **argv)
{
    // Car s1;
    Car s1 = Car();
    s1.dodaj();
    s1.dane();
    
    Car s2 = Car("Opel", "Astra", 1998, 220000);
    s2.dane();

    return 0;
}

