from itertools import permutations
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        if N == 1:
            return True
        digits = [c for c in str(N)]
        perms = [int("".join(perm)) for perm in permutations(digits)  ]
        #dontexceed = 10 ** (len(digits))
        #print(list(perms))
        
        for perm in perms:
            while perm % 2 == 0:
                perm = perm // 2
                if perm == 1:
                    return True
        return False