class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        f = []
        for i in nums1:
            for j in nums2:
                    if i in nums1 and i in nums2 or i in nums2 and i in nums3 or i in nums1 and i in nums3:
                        f.append(i)
                    if j in nums1 and j in nums2 or j in nums2 and j in nums3 or j in nums1 and j in nums3:
                        f.append(j)
        return set(f)
        
