/*
// Name : Olawale Ayejuyuyone
// Creation : 08/31/2017
// Version : E1
// Description : Displays the message "Hello World"
***********************************************/
#include <iostream>
#include <string>
using namespace std ; // std :: cout

double area (double lenght, double width)
{
  return lenght * width;
}

double area (double radius)
{
  return 3.14159 * radius *radius;
}

int main()
{
  cout << area (1) << endl;
  cout << area (1,1) << endl;
  return 0; 
}
