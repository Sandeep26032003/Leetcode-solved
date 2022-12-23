class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while int(n) == n and n > 1:
            n = n / 2.0
        return n == 1
