class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(s.split()) != len(pattern):
            return False
        patternDict = {}
        strDict = {}
        s = s.split()
        for idx, word in enumerate(s):
            patternDict[pattern[idx]] = word
        print(patternDict)
        countPattern = Counter(patternDict.values())
        for idx, word in enumerate(s):
            if patternDict[pattern[idx]] != word or max(countPattern.values()) > 1:
                return False
        return True