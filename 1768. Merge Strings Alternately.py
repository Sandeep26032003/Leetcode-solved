class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1,w2=0,0
        r = ""
        while w1<len(word1) or w2<len(word2):
            if w1<len(word1):
                r+=word1[w1]
                w1+=1
            if w2<len(word2):
                r+=word2[w2]
                w2+=1
        return r
