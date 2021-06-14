class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dic = {w[::-1]: i for i, w in enumerate(words)}
        res = []
        #n = len(words)
        # store all possible palindromes to the dict
        for i, word in enumerate(words):
            
            if word in dic and dic[word] != i:
                res.append([i, dic[word]])
            for j in range(1, len(word)+1):
                if word[:-j] in dic and word[-j:] == word[::-1][:j]:
                    res.append((i,dic[word[:-j]]))
                if word[j:] in dic and word[:j] == word[::-1][-j:]:
                    res.append((dic[word[j:]], i))
#                 key = word[:-j][::-1] 
               
#                 if (word+key) == (word+key)[::-1]:
#                     if key in dic and dic[key] :
#                         dic[key].append(i)
#                     else:
#                         dic[key] = [i]
                
            #print(dic)
        return res