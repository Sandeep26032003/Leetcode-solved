class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        oddlist = []
        evenlist = []
        finalist = []
        for i in range(len(nums)):
            if i%2 == 0:
                evenlist.append(nums[i])
            else:
                oddlist.append(nums[i])
        evenlist.sort()
        oddlist.sort()
        oddlist=oddlist[::-1]
        ln=min(len(evenlist),len(oddlist))
        for i in range(ln):
            finalist.append(evenlist[i])
            finalist.append(oddlist[i])
        if len(evenlist)==ln:
            finalist+=oddlist[ln:]
        else:
            finalist+=evenlist[ln:]
        return finalist
