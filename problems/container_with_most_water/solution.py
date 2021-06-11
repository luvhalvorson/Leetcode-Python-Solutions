class Solution:
    def maxArea(self, height: List[int]) -> int:
        # sublistlen+1 * min(兩方端點)
        # themax = 0
        # if len(height) == 2:
        #     return min(height)*1
        # for sublen in range(len(height), 1, -1):
        #     for i in range(len(height)-sublen+1):
        #         themax = max(themax, (sublen-1)*min(height[i], height[i+sublen-1]))
        #         #rint(themax)      
        # return themax
        
        # l = 0
        # r = len(height) -1
        # water = 0
        # while l < r:
        #     water = max(water, min(height[l], height[r]) *(r-l) )
        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        #     #print(l, r, min(height[l], height[r]) *(r-l), water)
        # return water
        l = 0
        r = len(height) - 1
        max_area = 0
        hmax = max(height)
        while (r - l) * hmax >= max_area :
            if height[l] <= height[r] :
                area = height[l] * (r-l) 
                l = l + 1
            elif height[l] > height[r] :
                area = height[r] * (r-l)
                r = r - 1
            #else :
            #    area = height[l] * (r-l)
             #   l = l + 1
                
            if area > max_area :
                max_area = area
        return max_area