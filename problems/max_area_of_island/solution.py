class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        themax = 0
        m = len(grid)
        n = len(grid[0])
            
        def rec(i, j): 
            if grid[i][j] != 1: #0或-1 -1就不重複算了 
                return 0 
            count = 1
            grid[i][j] = -1 
            
            if i+1 < m: #下
                count += rec(i+1, j)
            if i-1 >= 0: #上
                count += rec(i-1, j)
            if j+1 < n: #又
                count += rec(i, j+1)
            if j-1 >= 0: #左
                count += rec(i, j-1)
            return count
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    themax = max(rec(i, j), themax)
        return themax