class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # 假設都要把f->t
        
        
        
        def help(target):
            curk = k
            curres = 0
            res = 0
            pos = []
            for i in range(len(answerKey)):
                if answerKey[i] == target:
                    curres += 1
                else:
                    pos.append(i)
                    if curk > 0:
                        curres += 1
                        curk -= 1
                    else:
                        res = max(curres, res)
                        curres = i - pos.pop(0)
                               
            res = max(res, curres)
            return res
        return max(help("T"), help("F"))