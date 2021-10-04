class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        s_stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                elif s_stack:
                    s_stack.pop()
                else:
                    return False
            else:
                s_stack.append((i))
                
        for i in stack[::-1]:
            if s_stack:
                s_i = s_stack.pop()
                if s_i < i:
                    return False
            else:
                return False
        return True