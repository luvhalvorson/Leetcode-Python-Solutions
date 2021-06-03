class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts.sort()
        verticalCuts.sort()
        #print(horizontalCuts,verticalCuts)
        hmax = horizontalCuts[0]
        vmax = verticalCuts[0]
        for i in range(1, len(horizontalCuts)):
            hmax = max(hmax, horizontalCuts[i] - horizontalCuts[i-1]) 
        for i in range(1, len(verticalCuts)):
            vmax = max(vmax, verticalCuts[i] - verticalCuts[i-1]) 
        vmax = max(vmax, w - verticalCuts[-1])
        hmax = max(hmax, h - horizontalCuts[-1])
        
        return (hmax * vmax)  % (10**9+7)
            