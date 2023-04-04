class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        else:
            while original in nums:
                original*=2
            return original
