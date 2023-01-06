class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        maximum = 0
        count=0
        for i in costs:
            maximum+=i
            if maximum <= coins:
                count+=1
        return count

