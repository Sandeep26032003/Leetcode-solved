class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1,l2 = [],[]
        for i in s:
            if i=="#" and l1:
                l1.pop()
            elif i=="#" and not l1:
                continue
            else:
                l1.append(i)
        for i in t:
            if i=="#" and l2:
                l2.pop()
            elif i=="#" and not l2:
                continue
            else:
                l2.append(i)
        return l1==l2
