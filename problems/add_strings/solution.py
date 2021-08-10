class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        c = 0
        res = ""
        while i >= 0 and j >= 0:
            s = int(num1[i]) + int(num2[j]) + c
            if s >= 10:
                c = 1
                s -= 10
            else:
                c = 0
            res = str(s) + res
            i-=1
            j-=1
        if j >= 0:
            res = str(int(num2[:j + 1]) + c) + res
        elif i >= 0:
            res = str(int(num1[:i + 1]) + c) + res
        elif c != 0:
            res = "1" + res
        return res