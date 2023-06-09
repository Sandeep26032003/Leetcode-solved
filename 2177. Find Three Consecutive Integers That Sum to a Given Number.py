class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        r = num//3
        ans = [r-1,r,r+1]
        if sum(ans) == num:
            return ans
        return []
