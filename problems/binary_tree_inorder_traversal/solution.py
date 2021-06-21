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
        res = []
        l = [root]
        cur = root.left
        while l or cur:
            while cur:
                l.append(cur)
                cur = cur.left
            t = l.pop() 
            res.append(t.val)
            cur = t.right
                
                          
        return res 