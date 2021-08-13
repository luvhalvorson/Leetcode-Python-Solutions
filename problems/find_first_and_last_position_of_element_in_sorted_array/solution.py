class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        start = None
        while l < r:
            mid = l + (r - l) // 2
            if target < nums[mid]:
                r = mid
            elif target == nums[mid]:
                if (mid == 0 or nums[mid - 1] != target):
                    start = mid
                    break
                else:
                    r = mid
            elif target > nums[mid]:
                l = mid + 1
        if start is None:
            return [-1, -1]
        l, r = start, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if target < nums[mid]:
                r = mid
            elif target == nums[mid]:
                if (mid == len(nums) - 1 or nums[mid + 1] != target):
                    #print("end", mid, r, nums[mid+1])
                    end = mid
                    break
                else:
                    l = mid + 1
            elif target > nums[mid]:
                l = mid + 1
        return [start, end]