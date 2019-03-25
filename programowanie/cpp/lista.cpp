/*
 * lista.cpp
 */


#include <iostream>
using namespace std;

struct node {
  int liczba;
  node * nast;  
};

int addToB() {
    node *glowa = NULL;
    node *nowy;
    
    while(czy() != 'n') {
        try {
            nowy = new node;
        } catch(bad_alloc) {
            cout << "Brak pamięci!" << endl;
            return -1;
        }
        nowy ->nast = glowa;
        nowy ->liczba = getD();
        glowa = nowy;
    }
}

int main(int argc, char **argv)
{
    addToB();
	return 0;
}

