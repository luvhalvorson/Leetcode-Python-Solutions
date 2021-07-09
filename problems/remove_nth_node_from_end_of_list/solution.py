# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        q = []
        p = head
        
        while p:
            q.append(p)
            if len(q) > n + 1:
                q.pop(0)
            p = p.next
        if len(q) == n + 1:
            q[0].next = q[0].next.next
        elif len(q) == 1:
            return None
        else:
            return q[-n+1]
        return head