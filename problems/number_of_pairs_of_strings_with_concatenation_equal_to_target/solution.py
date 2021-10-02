class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        #nums.sort(key=len)
        #print(nums)
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                #if len(target) - len(nums[i]) != len(nums[j]):
                    
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    res += 1
                    
        return res