
class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(x)[::-1]) if x >= 0 else -int(str(x)[:0:-1])
        return  rev if (rev< 2**31-1 and rev > -(2**31)) else 0
        