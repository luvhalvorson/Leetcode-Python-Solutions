import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set((0, 0))
        pq = [(grid[0][0], 0, 0)]
        res = 0
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while pq:
            T, i, j = heapq.heappop(pq)
            res = max(res, T)
            
            if i == j == n - 1:
                break
            for dir in directions:
                x, y = i + dir[0], j + dir[1]
                if x < 0 or x >= n or y < 0 or y >= n or (x, y) in visited:
                    continue
                heapq.heappush(pq, (grid[x][y], x, y))
                visited.add((x, y))
        return res
