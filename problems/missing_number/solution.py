class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x =  len(nums)
        thesum = x  * (x + 1) // 2
        for num in nums:
            thesum -= num
        return thesum