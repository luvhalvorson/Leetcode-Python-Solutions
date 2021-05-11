class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle :
            return 0
        
        neeleng = len(needle)
        for i in range(len(haystack)-len(needle)+1):
            
            if haystack[i:i+neeleng] == needle:
                return i
                                    
        return -1