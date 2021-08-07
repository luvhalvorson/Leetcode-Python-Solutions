from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for str in strs:
            mylist = [0] * 26
            for c in str:
                mylist[ord(c) - ord('a')] += 1
            if tuple(mylist) in hashmap:
                hashmap[tuple(mylist)].append(str)
            else:
                hashmap[tuple(mylist)] = [str]     
        return list(hashmap.values())
            