class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        #csquare = [i**2 for i in range(1, n + 1)]
        for a in range(1, n + 1):
            for b in range(a, n + 1):
                ab = a** 2 + b ** 2
                sqrt = math.ceil(ab ** (0.5))
                if sqrt > n:
                    break
                if ab == sqrt ** 2:
                    res += 2
                
        return res