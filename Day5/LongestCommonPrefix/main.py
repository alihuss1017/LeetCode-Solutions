class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        count = 0
        prefix = ""
        while True:
            for word in strs:
                if count == len(min(strs, key = len)) or not word.startswith(strs[0][0:count + 1]):
                    return prefix
            prefix += strs[0][count]
            count += 1
