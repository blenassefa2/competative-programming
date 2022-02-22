# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nw = ListNode()
        temp =nw
        if not head or not head.next:
            return head
        
        if head and head.next and head.next.next:
            while head.next.next:
                p = ListNode(head.next.val,ListNode(head.val))
                temp.next = p
                temp = temp.next.next
                head =head.next.next
                if not head.next:
                    break
                    
        if head and head.next:
            temp.next = ListNode(head.next.val,ListNode(head.val))
        elif head:
            temp.next = head
            
        return nw.next