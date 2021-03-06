class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        '''for i in range(len(words)):
            words[i] = words[i][::-1]'''
        words = [word[::-1] for word in words]
        words.sort(reverse=True)
        print(words)
        result = len(words[0]) + 1
        print(result)
        for i in range(1, len(words)):
            if words[i-1][:len(words[i])] != words[i]:
                result += (len(words[i]) + 1)
                print(result)
        return result