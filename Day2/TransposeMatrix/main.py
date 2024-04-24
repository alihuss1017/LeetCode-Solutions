class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        copy = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                copy[j][i] = matrix[i][j]
        return copy