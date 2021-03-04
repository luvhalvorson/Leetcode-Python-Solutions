# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p_a = headA
        p_b = headB
        # A + common + B + common
        # B + common + A + common
        flag = 1
        while p_a != p_b:
           # p_a = p_a.next if p_a else headB
            #p_b = p_b.next if p_b else headA
            p_a = headB if not p_a else p_a.next
            p_b = headA if not p_b else p_b.next
        return p_a