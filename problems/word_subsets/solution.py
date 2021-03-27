class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bset = {}
        for b in B:
            c=  Counter(b)
            for key in c:
                if key in bset:
                    bset[key] = max(c[key], bset[key])
                else:
                    bset[key] = c[key]
        print(bset)
        result = []
        for a in A:
            flag = 1
            for k in bset:
                if a.count(k) >= bset[k]:
                    continue
                else:
                    flag = 0
                    break
            if flag == 1:
                result.append(a)
        
        return result