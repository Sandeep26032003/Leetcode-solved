class Solution:
    def removeStars(self, s: str) -> str:
        lst = []
        for i in s:
            if i=="*" and lst:
                lst.pop()
            elif i=="*" and not lst:
                continue
            else:
                lst.append(i)
        return "".join(lst)
        
