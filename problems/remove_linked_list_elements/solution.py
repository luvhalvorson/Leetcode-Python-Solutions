# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(next=head)
        c = dummy
        while c.next:
            if c.next.val == val:
                c.next = c.next.next
            else:
                c = c.next
        return dummy.next