/*
// Name : Olawale Ayejuyuyone
// Creation : 08/31/2017
// Version : E1
// Description : Displays the message "Hello World"
***********************************************/
#include <iostream>
#include <string>
using namespace std ; // std :: cout

void Hello(string name)
{
  cout << "Hello, " << name;
}

//Function name : area()
//Parameters: double length, double width
//Returns: the product of lenght and width
double area (double lenght, double width)
{
  double result= lenght * width;
  return result;
}

//Function name : PI()
//Parameters: None
//Returns: the mathematical Pi constant
double PI()
{
  return 3.14159;
}
/* Currently for all previous funtions we were passing
arguments by value. that means , the values of the arguments were copied
, and the copies were used in the function. To verify, we will create
a new functon ,swap, that switches the values of its Parameters. For the
first Version of swap , we will pass the arguments as we usually do ,
then check the values of the arguments before and after the call to swap.*/
// Funtion Name :swap()
//Parameters : int x, int y
//Return :Nothing
// Description : switches the values of x and y


void swap(int x, int y)
{
  cout <<"In function :Before \n";
  cout << "x = " << x << "y= " << y << endl;

  int temp =x ;
  x = y ;
  y= temp;

  cout << "In Function : After\n";
  cout <<"x= " << x << "y= " << y <<endl;

}


int main()
{
  Hello("Peter");
  cout <<endl;
  cout << area(5,4) <<"\n";
  cout << PI()<<endl;

  return 0;
}
