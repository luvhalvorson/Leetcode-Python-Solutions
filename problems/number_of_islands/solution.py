# 112 ms sample
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        c, r = len(grid), len(grid[0])
        def mark_visited(i, j):
            grid[i][j] = "2"
            if i > 0 and grid[i-1][j] == "1":
                mark_visited(i-1, j)
            if i < c - 1 and grid[i+1][j] == "1":
                mark_visited(i+1, j)
            if j > 0 and grid[i][j-1] == "1":
                mark_visited(i, j-1)
            if j < r - 1 and grid[i][j+1] == "1":
                mark_visited(i, j+1)
        res = 0
        for i in range(c):
            for j in range(r):
                if grid[i][j] == "1":
                    res += 1
                    mark_visited(i, j)
                # print(str(grid))
        return res 