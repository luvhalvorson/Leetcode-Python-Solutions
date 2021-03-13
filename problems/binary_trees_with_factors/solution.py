class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        num=0
        dic = {}
        for i in range(len(arr)):
            dic[arr[i]] = 1
            for j in range(0, len(arr)):
                if (arr[i] % arr[j] == 0) and arr[i] // arr[j] in dic:
                    dic[arr[i]] += dic[arr[j]] * dic[arr[i]//arr[j]]
            num += dic[arr[i]]
        #num=0
        #for k in dic:
        #    num += dic[k]
        return num % (10**9+7)