class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = 0
        for i in range(len(nums)+1):
            if i in nums:
                continue
            m+=i
        return m

            

