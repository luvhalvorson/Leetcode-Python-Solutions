class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [nums, [nums[1], nums[0]]]  
        res = []
        for i, num in enumerate(nums):

            res += [ [num] + l for l in self.permute(nums[: i] + nums[i + 1:])]
        return res
    
        # def help(listnums):
        #     if len(listnums) == 1:
        #         return [listnums]
        #     if len(listnums) == 2:
        #         return [listnums, [listnums[1], listnums[0]]]