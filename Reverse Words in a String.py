class Solution:
    def reverseWords(self, s: str) -> str:
        s1=" "
        s = s.split()
        s = s[::-1]
        s1 = s1.join(s)
        return s1
        
