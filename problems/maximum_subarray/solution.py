class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cursum, maxsum = nums[0], nums[0]
        for num in nums[1:]:
            if cursum + num > num:
                cursum += num
            else:
                cursum = num
            maxsum = max(maxsum, cursum)
        return maxsum
        