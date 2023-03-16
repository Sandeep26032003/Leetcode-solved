class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums1 = set(nums)
        lst=[]
        for i in range(1,len(nums)+1):
            if i in nums1:
                continue
            lst.append(i)
        return lst
