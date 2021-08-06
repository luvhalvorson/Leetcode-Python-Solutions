class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
        l = sorted(h.items(), key= lambda x: x[1], reverse=True)
        return [key[0] for key in l[:k]]