# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        if head.next is None:
           
            return head
        
        temp = head.next # store node2
        rest = temp.next # store node2's next node
        temp.next = head # node2 links to node1
        head.next = self.swapPairs(rest) # node1 links to the rest of the linkedlist 
        
        return temp
        