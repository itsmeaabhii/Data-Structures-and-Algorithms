from typing import List

class SelectionSort:
    def selectionSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        for i in range(n):
            min_index = i 
            
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            
            arr[i], arr[min_index] = arr[min_index], arr[i]
        
        return arr


obj = SelectionSort()
result = obj.selectionSort([5,3,2,6,7,1,9])
print(result)