class Solution:
    def romanToInt(self, s: str) -> int:
        prev = 0
        mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in s[::-1]:
            if mapping[i] >= prev:
                ans += mapping[i]
            else:
                ans -= mapping[i]
            prev = mapping[i]
        return ans
