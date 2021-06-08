class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        temp = num
        maskbit = 1
        while temp >> 1:
            temp = temp >> 1
            maskbit += 1
        #print()
        
        return num ^ ((1 << maskbit) -1)