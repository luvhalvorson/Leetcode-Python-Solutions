class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        
        ans = [0, 1]

        for i in range(2, n+1):
            # if i & 1 == 1: #基數 
            #     ans.append(ans[-1]+1) #一定是從偶數番最後一bit
            # else: #now is even how to build up from odd?
            #     flipbits = num[i-1] ^ num[i]
            #     flipbits & 1 == 1
            #     ans.append()
            ans.append(ans[i>>1]+(i%2))


        return ans
        