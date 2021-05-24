class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            else:
                dic.pop(num)
        res = [key for key in dic.keys()]
        return res[0]