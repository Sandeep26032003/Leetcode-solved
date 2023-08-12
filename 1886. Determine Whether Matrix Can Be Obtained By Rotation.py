class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        row = len(mat)
        col = len(mat[0])
        c = row+col
        while c:
            if mat == target:
                return True
                break
            else:
                mat_copy = [[0]*col for _ in range(row)]
                for i in range(row):
                    for j in range(col):
                        mat_copy[j][(row-1)-i] = mat[i][j]
                mat[:] = mat_copy[:]
                c-=1
        return False
            
