class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        ## dp?
        ## check if current is target
        ## no, then current + fuel>target
        # if current == target:
        #     solve
        # else:
        #     if current + fuel > target:
        #         solve
        #     else:
        #         if 
        # ## start with 0, stations00-
        # curpoint = 0
        # distance = stations[i][0] - stations[i-1][0]
        # if startFuel < distance:
        #     dp[i] = -1
        # dp[i] = dp[]
        res = 0
        i = 0
        n = len(stations)
        pq = []
        while startFuel < target:
            
            while (i < n and stations[i][0] <= startFuel):
                
                
                heapq.heappush(pq, -stations[i][1])
                i+=1
            
            if not pq:
            	return -1
            startFuel += -heapq.heappop(pq)
            res += 1
        
        return res