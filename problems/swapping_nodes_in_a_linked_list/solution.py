# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        temp = arr[k-1] 
        arr[k-1] = arr[-k]
        arr[-k] = temp
        
        cur2 = head
        for e in arr:
            cur2.val = e
            cur2 = cur2.next
        return head
            