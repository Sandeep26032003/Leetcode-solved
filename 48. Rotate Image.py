class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        ans = [[0]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                ans[j][(row-1)-i] = matrix[i][j]
        
        matrix[:] = ans[:]
        matrix[:]
            
