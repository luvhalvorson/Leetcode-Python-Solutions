class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curmax = themax = nums[0]
        for num in nums[1:]:
            curmax = max(curmax+num, num)
            themax = max(themax, curmax)
        return themax