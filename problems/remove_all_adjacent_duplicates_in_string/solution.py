class Solution:
    def removeDuplicates(self, s: str) -> str:
       # remove the largest 偶數 palidrom in the string?
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
        return "".join(stack)