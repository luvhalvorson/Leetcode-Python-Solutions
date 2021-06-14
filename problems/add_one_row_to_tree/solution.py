# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        
        curdepth = 1
        if not root:
            return TreeNode(val)
        if depth == 1:
            nh = TreeNode(val)
            nh.left = root
            return nh 
        q = [root]
        while q:
            if curdepth == (depth-1):
                break
                
            for _ in range(len(q), 0, -1):
                
                curnode = q.pop(0)
                
                if curnode.left:
                    q.append(curnode.left)
                if curnode.right:
                    q.append(curnode.right)
            
            curdepth += 1
            #print([node.val for node in q], curdepth-1)    
        #print(q)
        for node in q:
            
            if node.left:
                temp = node.left
                node.left = TreeNode(val=val, left=temp)
                #node.left.left = temp
            else:
                node.left = TreeNode(val)
            if node.right:
                temp = node.right
                node.right = TreeNode(val=val, right=temp)
                #node.right.right = temp
            else:
                node.right = TreeNode(val)
        return root