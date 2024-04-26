class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        output = 0
        for i in range(rowIndex + 1):
            ans.append([1] * (i + 1))

        if rowIndex < 2:
            return ans[rowIndex]

        for i in range(1, rowIndex + 1):
            for j in range(len(ans[i])):
                if j + 1 >= len(ans[i]) or i + 1 >= len(ans):
                    break
                ans[i + 1][j + 1] = ans[i][j] + ans[i][j + 1]
                
        return ans[rowIndex]