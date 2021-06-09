# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # # pre : root l r
        # # in: l root r
        # head = TreeNode(preorder[0])
        # p1 = 1
        # p2 = 0
        # leng = len(preorder)
        # if p1 == p2:
        #     head.left = TreeNode(preorder[p1])
        #     p1 += 1
        #     p2 += 2 # skip root
        # else
        def helper(pre_start, in_start, in_end):
            if pre_start > len(preorder) - 1 or in_start > in_end:
                return None
            root = TreeNode(preorder[pre_start])
            in_i = 0
            for i in range(in_start, in_end + 1):
                if inorder[i] == root.val:
                    in_i = i
            root.left = helper(pre_start + 1, in_start, in_i - 1)
            root.right = helper(pre_start + in_i - in_start + 1 , in_i + 1, in_end)
            return root
        return helper(0, 0, len(inorder) - 1)