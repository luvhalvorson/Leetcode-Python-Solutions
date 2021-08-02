class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        s = [heights[-1]]
        for i in range(len(heights) - 2, -1, -1):

            

            j = 0
            #print(s)
            f = 0
            # while j < len(s) and s[j] >= heights[i]:
            #     f = 1                
            #     ans[i] -= 1
            #     j += 1 # if the top of stack higher than current one, then it can only see the one right next to it.            
            # #print(ans[i])
            # if f:
            #     ans[i] += 1
            while s and s[-1] < heights[i]: # pop until the current one can be pushed and keep monotonic
                ans[i] += 1
                s.pop()
            if s:
                ans[i] += 1
            s.append(heights[i])
        return ans