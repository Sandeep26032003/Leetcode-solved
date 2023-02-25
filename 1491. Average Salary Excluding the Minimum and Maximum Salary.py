class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        del salary[0]
        del salary[len(salary)-1]
        return sum(salary)/len(salary)
