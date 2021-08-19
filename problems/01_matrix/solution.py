import math
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        dp = [[math.inf] * (len(mat[0])) for _ in range(len(mat))]
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    dp[r][c] = 0
                else:             
                    if r == 0 and c == 0:
                        continue
                    elif r == 0:
                        dp[r][c] =   1 + dp[r][c-1]
                    elif c == 0:
                        dp[r][c] =  1 + dp[r-1][c]
                    else:
                        dp[r][c] =  1 + min(dp[r][c-1], dp[r-1][c])
        #print(dp)  
        for r in range(len(mat)-1, -1, -1):
            for c in range(len(mat[0])-1, -1, -1):
                if r == (len(mat)-1) and c == len(mat[0])-1:
                    continue
                elif r == (len(mat)-1):
                    dp[r][c] =  min(dp[r][c], 1 + dp[r][c + 1])
                elif c == len(mat[0])-1:
                    dp[r][c] =  min(dp[r][c], 1 + dp[r + 1][c])
                else:
                    dp[r][c] = min(1+dp[r + 1][c], 1+dp[r][c + 1],dp[r][c])
        return dp