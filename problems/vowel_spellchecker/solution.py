class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        def todev(word):
            return "".join('*' if c.lower() in vowels else c.lower()
                           for c in word)

        words = set(wordlist)
        caps = {}
        vows = {}

        for word in wordlist:
            caps.setdefault(word.lower(), word)
            vows.setdefault(todev(word), word)

        def check(query):
            if query in words:
                return query
            lower = query.lower()
            if lower in caps:
                return caps[lower]
            devow = todev(lower)
            if devow in vows:
                return vows[devow]
            return ""
        return map(check, queries)
            