# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # if len(nums) == 0:
        #     return None
        def buildtree(nums):
            if not nums:
                return None
            rooti = len(nums) // 2
            root = TreeNode(nums[rooti])
            root.left = buildtree(nums[:rooti])
            root.right = buildtree(nums[rooti+1:])
            return root
        return buildtree(nums)
            
            