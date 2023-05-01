class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [i for i in range(1,n+1) if n%i ==0]
        if len(factors)<k:
            return -1
        return sorted(factors)[k-1]
