#include <iostream>
#include <fstream>

using namespace std;

ifstream f1("input.txt");
int N, num;
string name, year, toys, toy;

int main()
{
    setlocale(LC_ALL, "Russian");
    f1 >> N;
    string M[N][4];
    for(int i=0; i<N; i++){
        f1 >> name >> year >> num;
        getline(f1, toys); //��������� ������ ������
        toys = "";
        for(int j=0; j<num; j++){
            if(j) toys+=", ";
            getline(f1, toy);
            toys+=toy;
        }
        M[i][0] = name;
        M[i][1] = year;
        M[i][2] = to_string(num);
        M[i][3] = toys;
    }

    for(int i=0; i<N; i++){
        cout << "���: "<< M[i][0] << "; ��� ��������: " << M[i][1] << "; ���������� ������� �������: " << M[i][2] << "; �������: "<< M[i][3] << endl;
    }
}
