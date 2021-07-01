# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if p is None and q is None:
#             return True
#         if p is None or q is None:
#             return False
#         if p.val != q.val:
#             return False
        
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        if p is None and q is None:
            return True
        q1 = [p] if p else []
        q2 = [q] if q else []
        print(q1, q2)
        while q1 and q2:
            print(len(q1), len(q2))
            if len(q1) != len(q2):
                return False
            for _ in range(len(q1)):
                cur1 = q1.pop(0)
                cur2 = q2.pop(0)
                if cur1.val != cur2.val:
                    return False
                
                if cur1.left and cur2.left:
                    q1.append(cur1.left)
                    q2.append(cur2.left)
                elif not cur1.left and not cur2.left:
                    pass
                elif not cur1.left or not cur2.left:
                    return False
                
                if cur1.right and cur2.right:
                    q1.append(cur1.right)
                    q2.append(cur2.right)
                elif not cur1.right and not cur2.right:
                    pass
                elif not cur1.right or not cur2.right:
                    return False
        if len(q1) != len(q2):
                return False        
        
        return True