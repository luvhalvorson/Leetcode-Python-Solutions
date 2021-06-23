import bisect
import collections
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # i want to sort (from short to long) and iterate through words to find out that if I can categorize them from finding one is another's subsequence)
        # 
        m = dict()
        def isMatch(word, d):
            if word in m:
                return m[word]
            prev = -1
            for w in word:
                i = bisect.bisect_left(d[w], prev + 1)
                if i == len(d[w]):
                    return 0
                prev = d[w][i]
            m[word] = 1
            return 1
        
        d = collections.defaultdict(list)
        for i, w in enumerate(s):
            d[w].append(i)
        ans = [isMatch(word, d) for word in words]
        return sum(ans)
