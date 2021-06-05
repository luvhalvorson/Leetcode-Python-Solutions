class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for ss in range(1, len(arr) + len(arr)%2, 2):
            
            for i in range(len(arr)-ss+1):
                res+=sum(arr[i:i+ss])
                
        return res