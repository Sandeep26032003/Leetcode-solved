class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        distance=0;vis_count=0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])>d:
                    vis_count+=1
            if vis_count == len(arr2):
                distance +=1
            vis_count=0
        return distance
