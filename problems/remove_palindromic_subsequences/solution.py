class Solution:
    def ispalindrome(self, s):
        #if len(set(s)) == 1:
        #    return True
        
        for i in range(len(s)//2):
            if s[i] == s[-(i+1)]:
                continue
            else:
                return False
        return True
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        elif self.ispalindrome(s):
            return 1
        else:
            return 2
   