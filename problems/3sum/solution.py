from itertools import combinations 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            # 0的部分先不管
            l = i + 1
            r = len(nums) - 1
            ans = -nums[i]
            #print(nums)
            while l < r:
                #print(l, r)
                
                if nums[l] + nums[r] == ans:
                    #print(l, r, nums[l], nums[r])
                    if l == i+1:
                        res.append([nums[i], nums[l], nums[r]])
                    elif l > i+1 and nums[l] != nums[l-1]:
                        res.append([nums[i], nums[l], nums[r]])
                    
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < ans:
                    l += 1
                else:
                    r -= 1
        return res