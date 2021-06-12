class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        print(sum([a for a in chalk[:5596]]))
        sumofchalk = sum(chalk)
        print(sumofchalk)
        if k >= sumofchalk:
            remain = k % sumofchalk
            if remain == 0:
                return 0
        else:
            remain = k
        for i in range(len(chalk)):
            if remain < chalk[i]:
                return i
            elif remain == chalk[i]:
                return i+1
                break
            else:
                remain -= chalk[i]
                
                #print(i, remain)
        #print(remain)
