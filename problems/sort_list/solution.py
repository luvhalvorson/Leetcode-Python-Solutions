# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        fast = head.next
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        secondlist = slow.next
        slow.next = None
        def merge(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            dummy = ListNode()
            cur = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return dummy.next
      
        return merge(self.sortList(head), self.sortList(secondlist))
    
        
            
        
        