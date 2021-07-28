# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = ListNode(0) 
        node = res
        
        while True:
            smallest = None
            s_i = None
            for i,l in enumerate(lists):            
                if l:
                    if smallest is None or l.val < smallest:
                        smallest = l.val
                        s_i = i            
            if s_i is None:
                break
            node.next = ListNode(smallest)
            lists[s_i] = lists[s_i].next
            node = node.next
        return res.next
#         h = []
#         dummy = ListNode()
#         cur = dummy
#         flag = 1
#         while flag:
#             flag = 0
#             for i, node in enumerate(lists):
#                 if node:
#                     heapq.heappush(h, (node.val))
#                     lists[i] = node.next
#                     flag = 1
#         while h:
#             val = heapq.heappop(h)
#             cur.next = ListNode(val)
#             cur = cur.next
        
#         return dummy.next