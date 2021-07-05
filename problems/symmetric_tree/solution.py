# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = [root]
        f = 1
        while f:
            f = 0
            print([n.val if n is not None else n for n in q])
            for _ in range(len(q)):
                cur = q.pop(0)
                if cur:
                    if cur.left:
                        q.append(cur.left)
                        # to specify that there is not None val in the queue
                        f = 1
                    else:
                        q.append(None)
                    if cur.right:
                        q.append(cur.right)
                        f = 1
                    else:
                        q.append(None)
           
            if len(q) % 2:
                return False
            else:
                # check the current queue
                for i in range(len(q) // 2):
                    if q[i] is None and q[-(i+1)] is None:
                        continue
                    elif q[i] is None or q[-(i+1)] is None:
                        return False
                    if q[i].val != q[-(i+1)].val:
                        return False
        
        return True