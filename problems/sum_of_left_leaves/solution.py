# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = 0
        while q:       
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    if not cur.left.left and not cur.left.right:
                        res += cur.left.val
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return res
        # def help(root, flag):
        #     if not root:
        #         return 0
        #     if not root.left and not root.right:
        #         return root.val * flag
        #     return help(root.left, 1) + help(root.right, 0)
        # return help(root, 0)