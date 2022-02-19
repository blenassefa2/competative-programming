class Linked:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def display(head):
        
        while head:
            print(head.data)
            head = head.next
    def Add(head,val):
        while head.next:
            head = head.next
        temp = Linked(val)
        head.next = temp
    def middle(head):
        heir = head
        turtle = head
        while heir.next:
            turtle = turtle.next
            heir = (heir.next).next
        print(turtle.data)

li =  Linked(3)


Linked.Add(li,4)
Linked.Add(li,7)
Linked.Add(li,3)
Linked.display(li)

