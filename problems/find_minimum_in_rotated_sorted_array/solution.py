class Solution:
    def findMin(self, nums: List[int]) -> int:
#         1 2 3 4 5  135
#         5 1 2 3 4  524
#         3 4 5 1 2  352
#         3 4 0 1 2   302
        
#         2 3 4 5 1
        
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l) // 2
            if nums[l] > nums[mid]:
                r = mid
            if nums[l] <= nums[mid]:
                if nums[r] > nums[mid]:
                    r = mid
                else:
                    l = mid + 1
        return nums[l]