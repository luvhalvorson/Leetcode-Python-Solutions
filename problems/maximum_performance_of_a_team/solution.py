import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        sortedlist = sorted(zip(efficiency, speed), reverse=True)
        
        #print("s", sortedlist[1])
        #print("e", sortedlist[0])
        
        res = -1
        minheap = []
        heaplen = 0
        curmaxsum = 0
        for e, s in sortedlist:
                heappush(minheap, s)
                heaplen += 1
                # get i+1 ppl if < k else get k ppl
                if heaplen <= k :
                    curmaxsum += s
                else:
                    curmaxsum += s - heappop(minheap)
                #curmaxsum += s if  heaplen <= k else s - heapop(myheap)
                #print("min", minheap, e,s)
                
                res = max(res, e * curmaxsum)
                #print("curmaxsum", curmaxsum, res)
        return (res % (10**9+7))