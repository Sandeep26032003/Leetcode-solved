class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decomlist=[]
        for i in range(1,len(nums),2):
            decomlist.extend([nums[i]]*nums[i-1])
        return decomlist
