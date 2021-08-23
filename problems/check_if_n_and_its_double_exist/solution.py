class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = set()
        for num in arr:
            if 2 * num in d:
                return True
            if num % 2 == 0 and num // 2 in d:
                    return True
            d.add(num)
        return False