class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        alt = [0]*(n+1)

        for i in range(1,n+1):
            alt[i] = gain[i-1] + alt[i-1]
        return max(alt)
