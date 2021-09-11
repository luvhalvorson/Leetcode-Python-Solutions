class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        
        res = 0
        for i in range(len(num1)):
            int1 = ord(num1[i]) - ord("0")
            for j in range(len(num2)):
                int2 = ord(num2[j]) - ord("0")
                digit = len(num2) - j - 1 + (len(num1) - i - 1)
                res += (int1 * int2) * (10**digit)
                
        return str(res)
            
            