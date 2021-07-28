class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return [nums, [nums[1], nums[0]] ]
            else:
                return [nums]
        nums = sorted(nums)
        res = []
        res += [[nums[0]] + l for l in self.permuteUnique(nums[1:])]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            res += [[nums[i]] + l for l in self.permuteUnique(nums[: i] + nums[i+1:])]
        return res