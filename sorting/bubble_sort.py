from typing import List

class BubbleSort:
    def bubblesort(self, arr:List[int])->(List[int]):
        for i in range(len(arr)-1, -1, -1):
            for j in range(i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        
        return arr



obj = BubbleSort()
result = obj.bubblesort([5,3,2,6,7,1,9])
print(result)