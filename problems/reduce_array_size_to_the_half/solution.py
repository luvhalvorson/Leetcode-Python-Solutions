class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        dic = sorted(dic.values(), reverse=True)
        #print(dic)
        res = 0
        sum = 0
        
        for v in dic:
            sum += v
            res += 1
            if sum >= len(arr) // 2:
                return res
        return res