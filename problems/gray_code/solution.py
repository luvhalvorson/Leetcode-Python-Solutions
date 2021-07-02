class Solution:
    def grayCode(self, n: int) -> List[int]:
        dp = ['0', '1']
        if n==1:
            return [int(s, 2) for s in dp]
        for i in range(n-1):
            dp += (dp[::-1])
            print(dp)
            for j in range(len(dp)):
                if j < len(dp)//2:
                     dp[j] = "0" + dp[j]
                else:
                     dp[j] = "1" + dp[j]
        return [int(s, 2) for s in dp]
#         def help(n):
#             if n == 1:
#                 return ['0', '1']

#             last = help(n-1) 
#             last += (last[::-1])

#             for i in range(len(last)):
#                 if i < len(last)//2:
#                     last[i] = "0" + last[i]
#                 else:
#                     last[i] = "1" + last[i]
#             print(last)
#             return last
#         return [int(s, 2) for s in help(n)]