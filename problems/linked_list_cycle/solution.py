# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = ListNode(1)
        while head != visited and head is not None:
            
            temp = head.next
            head.next = visited
            head = temp
        return True if head == visited else False