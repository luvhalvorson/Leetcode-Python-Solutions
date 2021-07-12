class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dic = {'2':'abc' , '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        res = [c for c in dic[digits[0]]]
        for d in digits[1:]:
            last = res
            cur = []
            for c in dic[d]:
                cur += [s + c for s in last]
                #print(cur)
            res = cur
        return res