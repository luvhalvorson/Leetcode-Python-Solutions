class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, c in enumerate(s):
            if c in d:
                d[c][1] = i
            else:
                d[c] = [i, i]

        res = []
        print(d)
        pair = []
        for v in d.values():                     
            if not res:
                pair = v
                res.append(v[1] - v[0] + 1)                
            else:          
                if v[0] < pair[1]:
                    if v[1] > pair[1]:
                        res[-1] += v[1] - pair[1]
                        pair[1] = v[1]  
                else:
                    res.append(v[1] - v[0] + 1)
                    pair = v
        return res