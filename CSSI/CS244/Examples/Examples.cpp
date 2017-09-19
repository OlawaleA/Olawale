/*
// Name : Olawale Ayejuyuyone
// Creation : 08/31/2017
// Version : E1
// Description : Displays the message "Hello World"
***********************************************/
//#include <iostream>
//using namespace std ; // std :: cout

//int main()
//{
	//cout << " Hello World!\n";
	//return 0;
//}
#include <iostream>
using namespace std ; // std :: cout

double perimeter (double s1, double s2, double s3, double s4= 0, double s5= 0, double s6=0)
{
	return s1+s2+s3+s4+s5+s6;
}

int main()
{
	double s1=1 , s2=2, s3=3, s4=4, s5=5, s6=6;
	cout<< perimeter (s1,s2,s3)<< endl;
	cout<< perimeter (s1,s2,s3,s4)<< endl;
	cout<< perimeter (s1,s2,s3,s4,s5)<< endl;
	cout<< perimeter (s1,s2,s3,s4,s5,s6)<< endl;
	return 0;
}
