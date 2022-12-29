class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        c1 = set(c)
        for i in c1:
            if c[i]>(len(nums)//2):
                return i
