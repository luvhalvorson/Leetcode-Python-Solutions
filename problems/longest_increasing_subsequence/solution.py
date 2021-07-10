class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxcount = 0
        dp = [1] * len(nums) 
        for i in range(len(nums)):
            
            for j in range(i):
                if nums[j] < nums[i]: 
                    dp[i] = max(dp[i], dp[j] + 1) 
            maxcount = max(maxcount, dp[i])
        return maxcount