class Solution:
    def frequencySort(self, s: str) -> str:
        # t 1 r 1 e 2
        # 1:tr 2:e 
        if len(s) == 1:
            return s
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        sort_d = sorted(d.items(), key=lambda x:x[1], reverse=True)
        s = []
        for k,v in sort_d:
            s.append(k*v)
        return "".join(s)