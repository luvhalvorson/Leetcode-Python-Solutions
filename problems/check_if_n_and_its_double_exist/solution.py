class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        arr.sort(key=lambda k:abs(k))
        for i in arr:
            if i in seen:
                return True
            else:
                seen.add(2*i)
        return False