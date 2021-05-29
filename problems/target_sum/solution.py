class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        nums = [0]+nums
        @lru_cache(None)
        def dp(i, total):
            if i == 0: return total == 0
            #print(f"current {i} {total}")
            #print(i-1, total - nums[i])
            #print(i-1, total + nums[i])
            return dp(i-1, total - nums[i]) + dp(i-1, total + nums[i])
            
        return dp(len(nums)-1, S)