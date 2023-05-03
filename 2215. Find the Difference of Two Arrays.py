class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result=[]
        l=[]
        l1=[]
        for i in nums1:
            if i not in nums2:
                l.append(i)
        result.append(list(set(l)))

        for i in nums2:
            if i not in nums1:
                l1.append(i)
        result.append(list(set(l1)))

        return (result)
