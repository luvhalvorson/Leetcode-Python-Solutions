# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [root]
        res = 1
        while q:
            for _ in range(len(q)):
                cur = q.pop(0)
                if (not cur.left) and (not cur.right):
                    return res
                if cur.left:
                    q.append(cur.left)     
                if cur.right:
                    q.append(cur.right)  
            
            res += 1
        return res
#         if not root:
#             return 0
        
#         l = self.minDepth(root.left)
#         r = self.minDepth(root.right)
#         return  1 + min(l, r) if l*r!=0 else 1 + l + r