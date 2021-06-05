class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        deadends = set(deadends)
        visited = {"0000"}
        q = ["0000"]
        res = 0
        
        while q:
            res += 1
            for _ in range(len(q), 0, -1): # pop the original queues (without added ones in this iteration)
                t = q.pop(0)
                for i in range(len(t)): # rotate each bit by 1 -1, see if achieve target, add it to q if not done or not seen
                    
                    # rotate from last state
                    s1 = t[:i] + str((int(t[i]) + 1) % 10) + t[i+1:] #-1
                    s2 = t[:i] + str((int(t[i]) - 1) % 10) + t[i+1:] #+1
                  
                    if (s1 == target or s2 == target) :
                        return res
                    if (s1 not in visited and s1 not in deadends) :
                        q.append(s1)
                    if (s2 not in visited and s2 not in deadends) :
                        q.append(s2)
                    visited.add(s1)
                    visited.add(s2)
            
        return -1