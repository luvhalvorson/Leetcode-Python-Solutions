class Solution:
    def isHappy(self, n: int) -> bool:
        past = []
        past.append(sum([n**2 for n in map(int, str(n))]))
        while past[-1] != 1:
            if (len(str(past[-1]**2)) == 1):
                return False
            cur = sum([n**2 for n in map(int, str(past[-1]))])
            if (len(past)>1 and cur in past):
                return False
            past.append(cur)
                    
        return True