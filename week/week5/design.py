class node:
    def __init__(self, val = 0, Next = None):
        self.val = val
        self.next = Next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        temp = self.head
        count = 0 
        while temp:
            if count == index:
                return temp.val
            count += 1
            temp = temp.next
    
    def addAtHead(self, val: int) -> None:
        n = node(val, self.head)
        self.head = n
        self.size +=1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return 
        if index == 0:
            self.addAtHead(val)
            return
        temp = self.head
        count = 0 
        while temp:
            if count == index - 1:
                n = node(val,(temp.next))
                temp.next = n
                self.size +=1
                break
            count += 1
            temp = temp.next
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        if index == 0:
            self.head = self.head.next
        
        temp = self.head
        count = 0 
        while temp:
            if count == index - 1:
                temp.next =temp.next.next
                
                break
            count += 1
            temp = temp.next
        self.size -=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)