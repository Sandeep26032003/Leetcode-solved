class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        lst=[]
        for i in strs:
            if i.isnumeric():lst.append(int(i))
            else:lst.append(len(i))
        return max(lst)
