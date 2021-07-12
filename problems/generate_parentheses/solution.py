class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(left, right, term):
            if left == n and right == n:
                res.append(term)
                return
            if left < n:
                backtrack(left + 1, right, term+"(")
            if right < left:
                backtrack(left, right + 1, term+")")
        backtrack(0, 0, "")
        return res