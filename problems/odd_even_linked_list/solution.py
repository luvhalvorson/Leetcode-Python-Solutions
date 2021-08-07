# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head
        even = head.next
        evenhead = even
        
        i = 1
        while odd and even:
            if i % 2  == 1:
                odd.next = even.next
                if not odd.next:
                    break
                else:
                    odd = odd.next
            else:
                even.next = odd.next
                even = even.next
            i += 1
        odd.next = evenhead
        return head