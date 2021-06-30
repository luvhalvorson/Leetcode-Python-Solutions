class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        threezeros = []
        curk = 0
        startindex = 0 
        maxlen ,curlen = 0,0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                if curk < k:
                    curk += 1       
                    #threezeros.append(i)
                else:
                    if not threezeros:
                        curlen = 0
                        continue
                    lastzeroi = threezeros.pop(0) 
                    curlen -= (lastzeroi - startindex + 1)
                    
                    startindex = lastzeroi + 1
                    #print(curk, lastzeroi, startindex,curlen)
                threezeros.append(i)
            curlen += 1
            maxlen = max(maxlen, curlen)
        #print(maxlen)
        return maxlen
            #threezeros.pop() - startindex