class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for val in operations:
            if val == 'C':
                ans.pop()
            
            elif val == 'D':
                ans.append(ans[-1] * 2)

            elif val == '+':
                ans.append(ans[-1] + ans[-2])

            elif val.isdigit() or (val[1].isdigit() and val.startswith('-')):
                ans.append(int(val))
        return sum(ans)
