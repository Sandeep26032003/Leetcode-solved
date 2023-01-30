class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c = 1,0,0
        for i in range(n):
            temp = a+b+c
            a=b
            b=c
            c = temp
            print(c)
        return c

        
