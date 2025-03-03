import random

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    def push(self, val):
        self.heap.append(val)
        size = len(self.heap)
        self.__shift_up(size - 1)

    def __shift_up(self, i):
        while (i - 1) // 2 >= 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2
    
    def pop_head(self):
        if not self.heap:
            raise IndexError("No heap")

        size = len(self.heap)
        self.heap[0], self.heap[size - 1] = self.heap[size - 1], self.heap[0]
        val = self.heap.pop()
        size -= 1

        self.__shift_down(0, size)

        return val
    
    def __shift_down(self, i, n):
        while 2 * i + 1 < n:
            left, right = 2 * i + 1, 2 * i + 2

            if 2 * i + 2 >= n:
                larger = left
            else:
                larger = left if self.heap[left] >= self.heap[right] else right

            if self.heap[i] < self.heap[larger]:
                self.heap[i], self.heap[larger] = self.heap[larger], self.heap[i]
                i = larger
            else:
                break
    
    def __init_heap(self, nums):
        size = len(nums)

        for i in range(size):
            self.heap.append(nums[i])
        
        for i in range((size - 2) // 2, -1, -1):
            self.__shift_down(i, size)

    def maxHeapSort(self, nums):
        self.__init_heap(nums)

        size = len(self.heap)
        
        for i in range(size - 1, -1, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.__shift_down(0 ,i)
        
        return self.heap

class AdSort:
    def __init__(self, nums = None):
        self.nums = nums

    def randomPartition(self, nums, low, high):
        i = random.randint(low, high)
        nums[i], nums[low] = nums[low], nums[i]
        return self.partition(nums, low, high)
    
    def partition(self, nums, low, high):
        pivot = nums[low]

        i, j = low, high
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            while i < j and nums[i] <= pivot:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[low] = nums[low], nums[i]

        return i

    def quickSort(self, nums, low, high):
        if low < high:
            pivot_i = self.randomPartition(nums, low, high)
            self.quickSort(nums, low, pivot_i - 1)
            self.quickSort(nums, pivot_i + 1, high)
        
        return nums
    
    def HeapSort(self, nums):
        myheap = MaxHeap()
        return myheap.maxHeapSort(nums)

s = AdSort([10, 25, 6, 8, 7, 1, 20, 23, 16, 19, 17, 3, 18, 14])
print(s.HeapSort(s.nums))