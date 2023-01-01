class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        s1 = ""
        j=0
        for i in range(k):
            s1+=s[i]
            j+=1
            if j != k:
                s1+=" "
        return s1
