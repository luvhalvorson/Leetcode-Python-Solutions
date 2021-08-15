class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(start_i, target, path, res):
            if target == 0:
                res.append(path)
            elif target < 0:
                return
            while start_i < len(candidates):
                dfs(start_i, target - candidates[start_i], path + [candidates[start_i]], res)
                start_i += 1
        dfs(0, target, [], res)
        return res
        # candidates.sort()
        # dp = [[] for _ in range(target)]
        # for i in range(target):
        #     #theset = set()
        #     for j in range(len(candidates)):
        #         if candidates[j] > i + 1:
        #             break
        #         #if candidates[j] in theset:
        #         #    continue
        #         curtarget = i + 1 - candidates[j]
        #         #theset.add(curtarget)
        #         if curtarget == 0:
        #             dp[i] += [[candidates[j]]]
        #         if curtarget > 0:
        #             dp[i] += [ [candidates[j]] + e  for e in dp[curtarget - 1] if e[0] >= candidates[j]]
        #     #print(dp[i])
        # return dp[-1]
