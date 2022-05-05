#include <iostream>
using namespace std;
#include <string>

int func1(int);
int func1();
int main() {

    int num;
    cout<<"Please enter a number : "<<endl;
    cin>>num;
    cout<<func1(num)<<endl;
    cout<<func1()<<endl;
    return 0;
}
int func1(int num){
    if (num==0) {
        return 1;
    }
    else {
      return (( (num / (num + 2)) - 10)* func1(num-1));
    }
    }


int func1() {
    double num;
    cout<<"Please enter a number : "<<endl;
    cin >> num;
    if (num == 0) {
        return 1;
    }
        else{
        return (( (num / (num + 2)) - 10)* func1(num-1));


        }
    }

