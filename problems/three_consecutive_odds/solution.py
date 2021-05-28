class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        leng = len(arr)
        for i in range(2, leng):
            if arr[i] % 2 == 1:
                if (arr[i-1] % 2 == 1) and (arr[i-2] % 2 == 1):
                    return True
            else:
                i+=3
                
                if i < leng:
                    continue
                else:
                    break
        return False