"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        q = [root]
        res = []
        cur = None

        while q:
            temp = []
            for _ in range(len(q)):
                cur = q.pop(0)
                temp.append(cur.val)
                q += (cur.children)

            res.append(temp)
        return res