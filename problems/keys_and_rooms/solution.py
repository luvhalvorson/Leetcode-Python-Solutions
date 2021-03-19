class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [0] * len(rooms)
        self.dfs(rooms, 0, visited)
        return sum(visited) == len(rooms)
        
    def dfs(self, rooms, index, visited):
        visited[index] = 1
        for key in rooms[index]:
            if not visited[key]:
                self.dfs(rooms, key, visited)
