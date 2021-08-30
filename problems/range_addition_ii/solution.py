class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        i = ops[0]
        #取交集
        #如果交集為空，連集。
        
        for a,b in ops[1:]:
            i[0] = min(i[0], a) 
            i[1] = min(i[1], b)
        return i[0] * i[1]