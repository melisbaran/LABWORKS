#include <iostream>
using namespace std;
#define MAX 100

class Node {
public:
    int data;
    Node *next;
    Node(int x, Node *n) {
        data = x;
        next = n;
    }
};
class Stack{
public:
    Node *top;
    int size;
Stack(){
top= nullptr;
size=0;
}
bool isEmpty(){
   if(top= nullptr){
       return true;
   } else{
       return false;
   }
}

void push(int e) {
    if (size == MAX) {
        cout << "Stack is full capacity:(";
    } else if (isEmpty()) {
        top = new Node(e, nullptr);
        size++;
        cout<<"Stack is empty";
    } else {
        Node *topNode = new Node(e, nullptr);
        topNode->next=top;
        top=topNode;
        size++;
    }

}

void wiewTop(){
    if (isEmpty()){
        cout<<"Stack is empty,top item cannot be displayed ";
    }
    else {
        cout << "Top item is: " << top << endl;

    }
}

void pop(){
    if (isEmpty()){
        cout<<"Stack is empty";
    }
    else{

        int x=top->data;
        Node *temp=top;
        top=top->next;
        delete temp;
        size--;
    }

}
int getSize(){
    return size;

}
void print() {
    Node *currentNode = top;
    while (currentNode != NULL) {
        cout << currentNode->data << " " << endl;
        currentNode = currentNode->next;
    }
}
};
    int main() {
        Stack *stack =new Stack();
        int input;
        do {
            cout << "Please enter a value to push/Press -1 to exit:" << endl;
            cin >> input;
            if (input != -1) {
                stack->push(input);
            }
        } while (input != -1&& stack->size!=MAX);
        cout<<"The stack size is : "<<endl;
        stack->getSize();
        cout<<"The stack: "<<endl;
        stack->print();
        cout<<"The top element is: ";
        stack->wiewTop();
        stack->pop();

        return 0;
    }

