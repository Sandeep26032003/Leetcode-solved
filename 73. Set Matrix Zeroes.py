class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        matrix_copy = [[0]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                matrix_copy[i][j] = matrix[i][j]

        def set_row(i):
            for j in range(col):
                if matrix_copy[i][j] !=0:
                    matrix_copy[i][j] = 0
                    
        def set_col(j):
            for i in range(row):
                if matrix_copy[i][j]!=0:
                    matrix_copy[i][j] = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    set_row(i)
                    set_col(j)
        matrix[:] = matrix_copy[:]
