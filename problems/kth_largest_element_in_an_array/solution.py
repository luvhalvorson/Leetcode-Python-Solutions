from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return sorted(nums, reverse=True)[k - 1]
       
        
        def partition(l, r):
            p_i = random.randint(l, r)
            nums[r], nums[p_i] = nums[p_i],  nums[r]            
            j = l
            for i in range(l, r):
                if nums[i] > nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            nums[j], nums[r] = nums[r], nums[j]
            return j
        l, r = 0, len(nums) - 1
        while l <= r:
            
            cur = partition(l, r)
            
            if  cur + 1 < k:
                l = cur + 1
            elif cur + 1 > k:
                r = cur - 1
            else:
                return nums[cur]
        