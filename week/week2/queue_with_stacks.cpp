#include<stdio.h>
#include<iostream>
class MyQueue {
    int Top;
    int array[11];
    int Top2;
    int array2[11];
public:
    MyQueue() {
        this->Top = 0;
        this->Top2 = 0;
    }
    
    void push(int x) {
        this->array[this->Top] = x;
        this->array2[this->Top + this->Top2] = x;
        
        this->Top++;
        
    }
    
    int pop() {
        int curr = this->Top2;
        int x = this->array2[curr];
        (this->Top2)++;
        this->Top--;
        return x;
    }
    
    int peek() {
        int curr = this->Top2;
        int x = this->array2[curr];
        return x;
    }
    
    bool empty() {
        if(this->Top ==0)
            return true;
        return false;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 */
int main ()
{
    
    MyQueue* obj = new MyQueue();
    obj->push(1);
    obj->push(2);
    obj->push(3);
    obj->push(4);
    int param_1 = obj->pop();
    obj->push(5);
    // int param_3 = obj->peek();
    // bool param_4 = obj->empty();
    int param_2 = obj->pop();
    int param_3 = obj->pop();
    int param_4 = obj->pop();
    int param_5 = obj->pop();
    printf("%i %i %i %i %i", param_1, param_2, param_3, param_4, param_5);
}
 