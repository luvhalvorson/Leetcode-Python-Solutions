import heapq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        q = collections.deque()
        q.append(0)

        for i in range(1, len(nums)):
            
            # #dp[i+1 : i+k+1]
            # while min 不在index內: # 好聰明 i dont need to mind it if it is not the value we are gonna use. instead, when we need to use it, then we check it. 
            #     # it is still be better if you find a way to add an element per time. 
            #     # but it is way better to think that should I remove the elemonts i dont need
            #     popheap()
            while q and q[0] < i-k:
                q.popleft()
            dp[i] = nums[i] + dp[q[0]]
            
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            q.append(i)
        print(q, dp)
        return dp[q[-1]]