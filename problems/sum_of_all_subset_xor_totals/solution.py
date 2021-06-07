
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def help(nums):
            if not nums:
                return []
           
            s = []
            for i in range(len(nums)):
                #print(i, nums[i])
                s.append(nums[i])
                #print(nums[i+1],nums, "hhh")
                s += [nums[i] ^ term for term in help(nums[i+1:])]
            return s
        
        return sum(help(nums))