from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums) ):
            ans += ([[nums[i]]] + [[nums[i]] + e for e in ans])
            print(ans)
        ans.append([])
        return ans