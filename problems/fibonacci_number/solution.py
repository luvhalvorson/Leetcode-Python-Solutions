class Solution:
    def fib(self, n: int) -> int:
        d = {}
        
        def helper(i):
            
            if i in d:
                return d[i]
            if i < 2:
                return i
            res =  helper(i-1) + helper(i-2)
            d[i] = res
            return res
        
        return helper(n)