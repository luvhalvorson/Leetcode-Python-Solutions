# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = head
        while head:            
            mynext = head.next
            while mynext and mynext.val == head.val: 
                mynext = mynext.next           
            head.next = mynext
            head = head.next
        return root