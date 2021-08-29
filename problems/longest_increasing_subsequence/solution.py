class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        maxcount = 0
        dp = [1] * len(nums) 
        for i in range(len(nums)):
            
            for j in range(i):
                if nums[j] < nums[i]: 
                    dp[i] = max(dp[i], dp[j] + 1) 
            maxcount = max(maxcount, dp[i])
        return maxcount
#         for i, num in enumerate(nums[::-1]):               
#             'Find leftmost value greater than x'
#             print(resdic)
#             first_bigger_i = bisect.bisect_right(btree, num)
#             if first_bigger_i != len(btree):
#                 res = 1 + resdic[btree[first_bigger_i]]                
#                 btree.insert(first_bigger_i, num)
#                 resdic[num] = res
#                 maxlen = max(maxlen, res)
#             else:        
#             # cant find first bigger
#             # list is empty or no nums bigger than cur
               
#                 resdic[num] = 1
#                 btree.insert(len(btree), num)

#         return maxlen   
 