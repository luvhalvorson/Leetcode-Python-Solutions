class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pointer = -1
        count = 0
        if s == " ":
            return 0
        while pointer >= -len(s):
            if s[pointer] != " ":
                count += 1
            else:
                if count == 0:
                    pass
                else:
                    break
            pointer -= 1
        return count