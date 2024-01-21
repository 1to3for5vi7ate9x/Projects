#include <iostream>
using namespace std;

int main() {
  char board[3][3];
  char input;
  int x,y; 

  for (int i=0; i < 3; i++) {
    for (int j=0; j < 3; j++) {
      board[i][j]=' ';
    }  
  }
  cout<<"Enter position x ";
  cin>>x;
  cout<<"Enter position y ";
  cin>>y;
  cout<<"Enter X or O ";
  cin>>input;
  if(input == 'X'){
  board[x][y] = 'X';
  }
  else {
  board[x][y] = 'O';
  }

  for (int i=0; i < 3; i++) {
    for (int j=0; j < 3; j++) {
      cout<<board[i][j]<<"| ";
    }
    cout<<endl<<"---------"<<endl;  
  }
  return 0;
}


