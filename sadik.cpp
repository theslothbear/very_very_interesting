#include <iostream>
#include <fstream>

using namespace std;
class Child
{
private:
    string nameM, yearM, toysM[10];
    int numM;
public:
    void print(){
        cout << "Имя: " << nameM << "; Год рождения: " << yearM << "; Количество игрушек: " << numM << " Игрушки: ";
        for(int i = 0; i < numM; i++){
            if(i) cout << ", ";
            cout << toysM[i];
        }
        cout << endl;
    }

    void setChild(string name, string year, int num, string toys[10]){
        nameM = name;
        yearM = year;
        numM = num;
        for(int i=0; i<num; i++){
            toysM[i] = toys[i];
        }
    }

    string* getToyNames(){
        return toysM;
    }

    string getName(){
        return nameM;
    }

    int getNum(){
        return numM;
    }
};

class Sadik
{
private:
    Child sp[100];
    int place=0;
public:
    void addChild(Child child){
       sp[place] = child;
       place++;
    }

    void findByToy(string toy_name){
        for(int i=0; i < place; i++){
            string *t = sp[i].getToyNames();
            for(int j=0; j<sp[i].getNum(); j++){
                if(toy_name == t[j]){
                    cout << sp[i].getName() << " ";
                    break;
                }
            }
        }
    }
    void findLessThan(int y){
        for(int i=0; i < place; i++){
            if (sp[i].getNum() < y) cout << sp[i].getName() << " ";
        }
    }
};

ifstream f1("input.txt");
string name, year, toys[10], ok, toy, toy_name;
int N, num, y;
int main()
{
    setlocale(LC_ALL, "Russian");
    f1 >> N;
    Sadik sad;
    for(int i=0; i<N; i++){
        Child obj;
        f1 >> name >> year >> num;
        getline(f1, ok);
        for(int j=0; j<num; j++){
            getline(f1, toy);
            toys[j]=toy;
        }
        obj.setChild(name, year, num, toys);
        //obj.print();
        sad.addChild(obj);
    }
    //getline(cin, toy_name);
    //sad.findByToy(toy_name);
    cin >> y;
    sad.findLessThan(y);
}
