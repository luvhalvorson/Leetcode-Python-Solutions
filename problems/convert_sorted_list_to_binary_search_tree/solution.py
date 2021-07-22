# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        #nums = []
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        p = head
        #本來忘記head已經走到None
        def buildtree(s, e):
            nonlocal p
            
            if s == e:
                return
            mid = (s+e)//2
            left = buildtree(s, mid)
            
            root = TreeNode(p.val)
            root.left = left
            p = p.next
            root.right = buildtree(mid + 1, e)
            
            
            return root
        return buildtree(0, length)