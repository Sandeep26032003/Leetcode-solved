class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        f = []
        for i in nums:
            if i != val:
                f.append(i)
        print(f)
        nums[:] = f
        
