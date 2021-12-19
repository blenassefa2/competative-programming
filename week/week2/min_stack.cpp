class MinStack {
    int Top;
    int array [100000];
public:
    MinStack() {
        Top = 0;
    }
    
    void push(int val) {
        this->array[this->Top] = val;
        this->Top++;
    }
    
    void pop() {
        this->Top--;
    }
    
    int top() {
        int curr = this->Top;
        int x = this->array[curr - 1];
        return(x);
    }
    
    int getMin() {
        int minimum =this->array[(this->Top) -1];
        for(int i = 0; i<this->Top; i++)
            if(minimum>this->array[i])
                minimum = this->array[i];
        return(minimum);
        
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */