# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        q = [root]
        res = []
        flag = 0
        while q:
            if flag == 0:
                res.append([node.val for node in q])
                flag = 1
            else:
                res.append([node.val for node in q[::-1]])
                flag = 0
            
            for _ in range(len(q)):
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
        return res
                
            
            