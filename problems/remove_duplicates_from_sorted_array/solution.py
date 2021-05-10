class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = None
        leng = 0
        for i in range(len(nums)-1, -1, -1):
            if temp == nums[i]:
                nums.pop(i)
            else:
                temp = nums[i]
                leng += 1 
        return leng