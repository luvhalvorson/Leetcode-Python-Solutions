# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if not head or not head.next:
        #     return head
        # newhead = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return newhead
        if not head or not head.next:
             return head
        dummy = ListNode()
        cur = dummy
        cur.next = head
        head = head.next
        cur.next.next = None
        
        while head:
            rest = cur.next
            cur.next = head
            head = head.next
            cur.next.next = rest
            
           
            
            
        return dummy.next