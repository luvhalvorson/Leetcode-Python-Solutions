from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = deque([('(',1,0)])
        while res[0][1]< n or res[0][2]< n:
            c, left, right = res.popleft()
            if left<n:
                res.append((c+'(', left+1, right))
            if right<n and left>right:
                res.append((c+')', left, right+1))
        return [r[0] for r in res]