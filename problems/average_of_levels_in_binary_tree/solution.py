# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        q = []
        q.append(root)
        
        while(q):
            sum, count = 0,0
            tlist = []
            while(q):
                
                temp = q.pop(0)
                sum += temp.val
                count += 1
                if temp.left:
                    tlist.append(temp.left)
                if temp.right:
                    tlist.append(temp.right)
            q = tlist
            result.append(sum / count)
            
        return result