class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        lastroom = len(rooms)
        mykeys = set([0])
        visited = set()
        def dfs(room_i):
            #print(f"we walk in {room_i} room with keys {mykeys}")
            if room_i in visited:
                #print("visited!",room_i, visited)
                return False
            [mykeys.add(key) for key in rooms[room_i]]
            # if we got all keys at the room, we are done(dont need to go to next room)
            if len(mykeys) == lastroom:
                #print("we got all keys at", room_i)
                return True
            visited.add(room_i)
            
            for key in rooms[room_i]:
                if dfs(key):
                    #print(key)
                    return True
            return False
        return dfs(0)