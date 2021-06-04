from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        if leng == 2: return [nums[0], 3-nums[0]]
        m = leng * (leng + 1) // 2 - sum(set(nums))
        c = Counter(nums)
        for n in c:
            if c[n] == 2:
                a = n
                break
        return [a, m]