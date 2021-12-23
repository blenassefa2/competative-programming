#define MAX 10000
class MyCircularDeque {
    int maximum;
    int size;
    int rear;
    int front;
    int que[MAX];
    
public:
    MyCircularDeque(int k) {
        this->size = 0;
        this->rear = -1;
        this->front = -1;
        this->maximum = k;
        
    }
    
    bool insertFront(int value) {
        if(this->size <this->maximum)
        {
            this->front--;
            if(this->front <= -1)
                this->front = maximum-1;
            this->que[this->front] = value;
            this->size++;
            if (this->rear <= -1)
            {
                this->rear = maximum -1;
            }
            return true;
        }
        return false;
    }
    
    bool insertLast(int value) {
        if(this->size < this->maximum)
        {
            this->rear++;
            if(this->rear == this->maximum)
                rear = 0;
            this->que[this->rear] = value;
            this->size++;
            if(this->front <= -1)
                this->front= 0;
            return true;
        }
        return false;
    }
    
    bool deleteFront() {
        if(this->size > 0)
        {
            this->front++;
            if(this->front == this->maximum)
                this->front = 0;
            this->size--;
            if (this->size == 0)
            {
                this->front = -1;
                this->rear = -1;
            }
            return true;
            
        }
        return false;
    }
    
    bool deleteLast() {
        if(this->size > 0)
        {
            this->rear--;
            if(this->rear <= -1)
                this->rear = this->maximum -1;
            this->size--;
            if (this->size == 0)
            {
                this->front = -1;
                this->rear = -1;
            }
            return true;
            
        }
        return false;
    }
    
    int getFront() {
        if (this->front>=0)
            return this->que[this->front];
        return -1;
    }
    
    int getRear() {
        if (this->rear>=0)
            return this->que[this->rear];
        return -1;
    }
    
    bool isEmpty() {
        if(this->size<=0)
            return true;
        return false;
    }
    
    bool isFull() {
        if(this->size ==this-> maximum)
            return true;
        return false;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */