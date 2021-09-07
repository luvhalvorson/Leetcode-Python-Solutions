# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
       
        while head:
            rest = dummy.next
            dummy.next = head
            head = head.next
            dummy.next.next = rest
            
        return dummy.next