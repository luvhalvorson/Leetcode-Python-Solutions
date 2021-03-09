# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        q = [root]
        
        curdep = 1
        if d == 1:
            return TreeNode(val=v, left=root)
            
        while q:
            # q is a list for current level
            temp = []
            while q:
                cur = q.pop(0)
                # get a node from last level and iterate its children
                if curdep == (d-1):
                    if cur.left:
                        tnode = cur.left
                        cur.left = TreeNode(val=v, left=tnode)
                    else:
                        cur.left = TreeNode(val=v)
                        
                    if cur.right:
                        tnode = cur.right
                        cur.right = TreeNode(val=v, right=tnode)
                    else:
                        cur.right = TreeNode(val=v)
                else:
                    
                    if cur.left:
                        temp.append(cur.left) 
                    if cur.right:
                        temp.append(cur.right)
                    
            if not temp:
                print("b")
                break
            q = temp
            curdep += 1

            #print( ([n.val for n in temp], curdep) if temp else "No") 
        return root