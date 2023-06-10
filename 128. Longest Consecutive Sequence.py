class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        lcs = 0
        for number in nums:
            if number-1 not in nums:
                length=0
                while (number+length) in nums:
                    length+=1
                lcs = max(lcs,length)
        return lcs
