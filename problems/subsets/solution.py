class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        l = self.subsets(nums[:-1])
        ans = [term + [nums[-1]] for term in l] + l
        return ans