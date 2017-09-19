/*
// Name : Olawale Ayejuyuyone
// Creation : 09/14/2017
// Version : E1
// Description : Switch Statements
***********************************************/
#include <iostream>
using namespace std;
/*
int main()
{
  char membership;
  cin >> membership;

  switch (membership)
  {
    case 'b':
    case 'B':
      cout << "10% off products \n";
      break;
    case 'g':
    case 'G':
      cout << "$100 gift card each year \n";
      break ;
    case 'p':
    case 'P':
      cout << "Free product each year \n";
    }
  }*/
  int main()
  {
    char membership;
    cin >> membership;

    switch (membership)
    {
      case 'p':
      case 'P':
        cout << "Free product each year\n";
      case 'g':
      case 'G':
        cout <<  "$100 gift card each year \n";
      case 'b':
      case 'B':
        cout << "10% off products \n";
        break;
      default:
        cout << "Error \n";
    }
      return 0;
  }
