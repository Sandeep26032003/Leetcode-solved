class Solution:
    def repeatedCharacter(self, s: str) -> str:
        lst=[]
        for i in s:
            if i not in lst:
                lst.append(i)
            else:
                return i
