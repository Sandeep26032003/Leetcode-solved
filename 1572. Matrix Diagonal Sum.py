class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans,n = 0,len(mat)
        for i in range(n):
            ans += mat[i][i] + mat[i][n-i-1]

        return ans - mat[n//2][n//2] if (n&1) != 0 else ans
