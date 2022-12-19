class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        num1=[]
        for i in range(len(num)):
            if num[i]=="1":
                num1.append(0)
            else:
                num1.append(1)
        num2 = ''.join([str(i) for i in num1])
        return int(num2,2)
