/*
 * bez nazwy2.cpp
 * 
 */


#include <iostream>
#include <cstdlib>
 
using namespace std;
 
int main()
{
  int n,m;
  string z,s;
  int szerokosc,wysokosc;
 
  cout << "SZEROKOSC=";
  cin >> szerokosc;
 
  cout << "WYSOKOSC=";
  cin >> wysokosc;
 
  cout << "BUDULEC: ";
  cin >> z;
 
  cout << "WNETRZE";
  cin >> s;
  cout << endl;
 
  for (n=0;n<szerokosc;n++)
     cout << z;
     cout << endl;
 
  for (m=0;m<wysokosc-2;m++)
    {
       cout << z;
          for (n=0;n<szerokosc-2;n++)
          cout << s;
          cout << z;
          cout << endl;
    }
  for (n=0;n<szerokosc;n++)
     cout << z;
     cout << endl;
 
  return 0;
}
