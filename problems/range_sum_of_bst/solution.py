# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        stack = [root]
        res = 0
        while stack:
            cur = stack.pop()
            if cur:
                if low < cur.val:
                    stack.append(cur.left)
                if high > cur.val:
                    stack.append(cur.right)
                if low <= cur.val <= high:
                    res += cur.val
        return res
#         if not root:
#             return 0
#         res = 0
        
#         if low > root.val:
#             res += self.rangeSumBST(root.right, low, high)
#         elif high < root.val:
#             res += self.rangeSumBST(root.left, low, high)
#         else:
#             res += self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + root.val

#         return res