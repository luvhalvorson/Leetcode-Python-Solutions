class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        sl = sorted(words, key=lambda x: x[::-1])
        #print(sl)
        res = 0
        for i in range(len(sl) - 1):
            # if i+1 > len(sl)-1:
            #     res += len(sl[i]) + 1
            #     break
            cur_word = sl[i]
            if cur_word == sl[i+1][-len(cur_word):]:
                continue
            else:
                res += len(sl[i]) + 1
        res += len(sl[-1]) + 1 
        return res