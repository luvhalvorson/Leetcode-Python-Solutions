# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        p1 = l1
        p2 = l2
        if p1.val < p2.val:
            chead = p1 
            p1 = p1.next
        else:
            chead = p2
            p2 = p2.next
        c = chead
        while p1 or p2:
            if p1 and p2:
                if p1.val < p2.val:
                    c.next = p1
                    p1 = p1.next
                else:
                    c.next = p2
                    p2 = p2.next
            else:
                c.next = p1 or p2
                break
            c = c.next
                
        return chead