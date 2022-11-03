class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum = 0
        for i in range(len(operations)):
            if operations[i] == "++X" or operations[i]=="X++":
                sum = sum+1
            else:
                sum = sum-1
        return sum
