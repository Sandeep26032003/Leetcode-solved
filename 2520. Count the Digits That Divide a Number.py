class Solution:
    def countDigits(self, num: int) -> int:
        t,c=num,0
        while t>0:
            s=t%10
            if num%s==0: c+=1
            t//=10
        return c
