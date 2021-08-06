# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        ## how to use recursive to break?
        # if not root:
        #     return 
        # if k == 0:
        #     res = root.val
        # if root.left:
        #     kthSmallest(root.left, k)
        # k -= 1  
        # if root.right:
        #     kthSmallest(root.right, k)
        # return res
        s = []
        cur = root
        c = 10
        while cur or s:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                a = s.pop()
                k -= 1
                if k ==0:
                    return a.val
                if a.right:
                    cur = a.right
        
#         while s or c!=0:
#             c -= 1
#             while cur:
#                 s.append(cur)
#                 print(cur.val, "pus")
#                 cur = cur.left
                
#             cur = s.pop()
#             #print(cur.val, s)
#             k -= 1
#             #if k == 0:
#                 #return cur.val
#             print(cur.val)
#             if cur.right:
#                 s.append(cur.right)
            