# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #A com+B+A
        #B+A+B
        p1 = headA
        p2 = headB
        while p1 or p2:
            if not p1:
                p1 = headB
            if not p2:
                p2 = headA
            if p1 is p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None