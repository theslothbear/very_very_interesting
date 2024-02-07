#include <iostream>
#include <fstream>

using namespace std;

ifstream f1("input.txt");
int N, num;
string name, year, toys, toy;
struct H{string nameM; string yearM; int numM; string toysM[10];};

void output(H child){
    cout << "Имя: " << child.nameM << "; Год рождения: " << child.yearM << "; Количество игрушек: " << child.numM << " Игрушки: ";
  for(int i = 0; i < child.numM; i++){
    if(i) cout << ", ";
    cout << child.toysM[i];
  }
  cout << endl;
}

int main()
{
    setlocale(LC_ALL, "Russian");
    f1 >> N;
    H M[N];
    for(int i=0; i<N; i++){
        f1 >> name >> year >> num;
        getline(f1, toys);
        toys = "";
        for(int j=0; j<num; j++){
            getline(f1, toy);
            M[i].toysM[j] = toy;
        }
        M[i].nameM = name;
        M[i].yearM = year;
        M[i].numM = num;
   }
   for(H child: M){
       output(child);
   }
}
