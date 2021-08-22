# 改成用default dict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        d = collections.defaultdict(list)
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)
       
        q = deque([start])
        visited = {start}
        while q:            
            cur = q.popleft()
            if cur == end:
                return True
            
            for node in d[cur]:                    
                if node not in visited:
                    q.append(node)
                    visited.add(node)
                          
        return False
            