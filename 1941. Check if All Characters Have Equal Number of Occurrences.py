class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)
        lst=[]
        for i in c.values():
            lst.append(i)
        return len(set(lst))==1
