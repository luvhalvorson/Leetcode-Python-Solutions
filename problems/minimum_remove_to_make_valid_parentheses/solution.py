class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                l.append(i)
            elif s[i] == ')':
                if l :
                    l.pop()
                else:
                    s[i] = ""
        #l = set(l) #光加set快12ms
        
        for i in l:
            s[i] = ""
        return "".join(s)

        #return "".join([s[i] for i in range(len(s)) if i not in l])