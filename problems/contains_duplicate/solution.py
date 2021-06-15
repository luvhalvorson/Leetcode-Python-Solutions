class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if nums.count(0) >= 2:
            return True
        return sum(nums) - sum(set(nums)) > 0