class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        p = 0
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        while p < len(s):
            
            if s[p] == "I":
                
                print("I")
                if p+1 < len(s):
                    if s[p+1] == "V":
                        res += 4
                        p += 2
                    elif s[p+1] == "X":
                        res += 9
                        p += 2
                    else:
                        res += 1
                        p += 1
                else:
                    res += 1
                    p += 1
                    break
                    
            elif s[p] == "X":
                if p+1 < len(s):
                    if s[p+1] == "L":
                        res += 40
                        p += 2
                    elif s[p+1] == "C":
                        res += 90
                        p += 2
                    else:
                        res += 10
                        p += 1  
                else:
                    res += 10
                    p += 1
            elif s[p] == "C":
                if p+1 < len(s):
                    if s[p+1] == "D":
                        res += 400
                        p += 2
                    elif s[p+1] == "M":
                        res += 900
                        p += 2
                    else:
                        res += 100
                        p += 1  
                else:
                        res += 100
                        p += 1  
            
            elif s[p] in dic:
                res += dic[s[p]]
                p+=1
            else:
                print(s[p])
        return res