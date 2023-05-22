class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}
        count=0
        for i in range(0,len(rings),2):
            if rings[i+1] not in rods:
                rods[rings[i+1]] = rings[i]
            else:
                rods[rings[i+1]] += rings[i]
        for rod,rings in rods.items():
            if 'B' in rings and 'R' in rings and 'G' in rings:
                count+=1
        return count
