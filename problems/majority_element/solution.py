class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = set(nums)
        return max(temp, key=nums.count)