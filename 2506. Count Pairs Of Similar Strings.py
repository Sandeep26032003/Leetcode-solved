class Solution:
    def similarPairs(self, words: List[str]) -> int:
        l,c=[],0
        for i in words:
            l.append(set(i))
        for i in range(len(l)+1):
            for j in range(i+1,len(l)):
                if l[i]==l[j]:
                    c+=1
        return c
