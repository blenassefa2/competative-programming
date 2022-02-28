# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for i in lists:
            temp = i
            while temp:
                l.append(temp.val)
                temp = temp.next
        l.sort()
        head = ListNode()
        temp= head
        for i in l:
            t = ListNode(i)
            temp.next = t
            temp = temp.next
        
        return head.next