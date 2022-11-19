class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        num1 = [num]
        for i in range(len(num)):
            if num[i]=="6":
                s=num.replace("6","9",1)
                num1.append(s)
            elif num[i]=="9":
                s=num.replace("9","6",1)
                num1.append(s)
        return max(num1)
