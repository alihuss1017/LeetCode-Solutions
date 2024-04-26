class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        output = 0
        for i in range(numRows):
            ans.append([1] * (i + 1))

        if numRows <= 2:
            return ans
        
        for i in range(1, numRows):
            for j in range(len(ans[i])):
                if j + 1 >= len(ans[i]) or i + 1 >= len(ans):
                    break
                ans[i + 1][j + 1] = ans[i][j] + ans[i][j + 1]
                
        return ans