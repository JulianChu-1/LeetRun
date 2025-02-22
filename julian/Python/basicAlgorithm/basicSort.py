
class MySort():
    def __init__(self):
        self.nums = [7, 2, 6, 8, 0, 4, 1, 5, 9, 3] 

    def bubbleSort(self, arr):
        for i in range(len(arr) - 1):
            flag = False # 优化：如果某次遍历没有发生
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = True
            if not flag:
                break

        return arr
    
    def selectionSort(self, arr):
        for i in range(len(arr) - 1):
            minIndex = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        
        return arr
    
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i
            while j > 0 and arr[j - 1] > temp:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = temp
        
        return arr

    def shellSort(self, arr):
        gap = len(arr) // 2

        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

        return arr
    
    def merge(self, left_nums, right_nums):
        nums = []
        
        while left_nums and right_nums:
            if left_nums[0] < right_nums[0]:
                nums.append(left_nums.pop(0))
            else:
                nums.append(right_nums.pop(0))
        
        while left_nums:
            nums.append(left_nums.pop(0))
        while right_nums:
            nums.append(right_nums.pop(0))

        return nums
    
    def mergeSort(self, arr):
        if len(arr) < 2:
            return arr
        
        mid = len(arr) // 2
        left_nums = self.mergeSort(arr[:mid])
        right_nums = self.mergeSort(arr[mid:])
        # print(left_nums)
        return self.merge(left_nums, right_nums)
        
    
sort = MySort()
print(sort.bubbleSort(sort.nums))
print(sort.selectionSort(sort.nums))
print(sort.insertionSort(sort.nums))
print(sort.shellSort(sort.nums))
print(sort.mergeSort(sort.nums))