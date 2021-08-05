
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         window = nums[:k]
        
#         q = [(-val, i) for i, val in enumerate(window)]
#         heapq.heapify(q)
#         res = [-q[0][0]]
#         for i in range(1, len(nums) - k + 1):
#             heapq.heappush(q, (- nums[i + k - 1], i + k - 1) )          
#             while q[0][1] < i: # q has at least k elements, would not be empty
#                 heapq.heappop(q)
#             res.append(-q[0][0])
#         return res
        if len(nums) == k:
            return [max(nums)]
        if k == 1:
            return nums
        q = deque()
        res = []
        for i in range(len(nums)):
            #print(q,"q1")
            #while q and q[0] < i - k + 1 :
            if q and q[0] == i-k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            #print(q,"q2")
            q.append(i)

            if i >= k - 1: # add result when the first window completed
                
                res.append(nums[q[0]])
        return res