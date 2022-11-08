class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = 0
        l = len(nums)-1
        while n<=l:
            m = int((n+l)/2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                n = m+1
            else:
                l = m-1
        return -1
