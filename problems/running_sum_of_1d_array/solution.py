class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        if len(nums) ==1 :
            return nums
        res = [nums[0]]
        for i in range(1, len(nums)):
            res.append(res[i-1] + nums[i])
        return res