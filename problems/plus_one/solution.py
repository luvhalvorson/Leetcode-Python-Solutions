class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digits[-1] += 1
        # for i in range(-1, -len(digits)-1, -1):
        #     if digits[i] >= 10:
        #         digits[i-1]
        #     else:
        #         break
       
        return list(str( int("".join(map(str,digits)))+1))