class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # if sum(matchsticks) % 4 != 0:
        #     return False
        # target = sum(matchsticks) // 4 
        # need_d = {}
        # for m in matchsticks:
        #     needmatch = target - m
        #     if m in need_d:
        #         need_d[m] -= 1 # someone needs me?               
        #     elif needmatch > 0:
        #         if needmatch in need_d: # does someone need the same thing as i
        #             need_d[needmatch] += 1
        #         else:
        #             need_d[needmatch] = 1
        # #print(need_d)
        # return sum(need_d.values()) == 0
        if not matchsticks or len(matchsticks) < 4:
            return False
        _sum = sum(matchsticks)
        div, mod = divmod(_sum, 4)
        if mod != 0 or max(matchsticks) > _sum / 4: return False
        matchsticks.sort(reverse = True)
        target = [div] * 4
        return self.dfs(matchsticks, 0, target)
        
    def dfs(self, matchsticks, index, target):
        if index == len(matchsticks): return True
        num = matchsticks[index]
        for i in range(4):
            if target[i] >= num:
                target[i] -= num
                if self.dfs(matchsticks, index + 1, target): return True
                target[i] += num
        return False