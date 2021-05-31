class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        i = 0
        
        try:
            while True:
                if nums[i] == 0:
                    del nums[i]
                    c +=1 
                else:
                    i+=1
        except:
            pass
        
        if c > 0:
            nums += [0]*c
        