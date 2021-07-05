class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        left = {'(':')', '[':']', '{':'}'}
        
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if not stack:
                    return False
                elif left[stack.pop()] != c:
                    return False
        return len(stack)==0