class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=[]
        for i in s.split():
            if i.isnumeric():
                l.append(int(i))
        return l == sorted(set(l))
