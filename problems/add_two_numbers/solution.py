# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        r = head
        c = 0
        while l1 or l2:
            if l1:
                a = l1.val
                l1 = l1.next
            else:
                a = 0
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
            
            
            r.next = ListNode((a + b + c) % 10)
            r = r.next
            c = (a + b + c) // 10
        if c == 1:
            r.next = ListNode(1)
        return head.next
            