# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        s = [root]
        res = []
        while s:
            cur = s.pop()
            while cur.left:
                s.append(cur)
                temp = cur
                cur = cur.left
                temp.left = None
            res.append(cur.val)
            if cur.right:
                s.append(cur.right)
        return res