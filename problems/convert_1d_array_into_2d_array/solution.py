class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        res = [[0] * n for _ in range(m)] 
        p = 0
        for i in range(m):
            for j in range(n):
                res[i][j] = original[p]
                p += 1
        return res