# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next : return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead
        # if not head : return None
        # c = head
        # pnode = None
        # while c:
        #     temp = c.next
        #     c.next = pnode
        #     pnode = c
        #     c = temp
        # return pnode
            
#         if not head:
#             return None
#         if not head.next:
#             return head
#         rest = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
        
#         return rest
