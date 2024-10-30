#前提是数组为有序数组，同时题目还强调数组中无重复元素，因为一旦有重复元素，使用二分查找法返回的元素下标可能不是唯一的
#写法1:左闭右闭
"""
第一种写法，我们定义 target 是在一个在左闭右闭的区间里，也就是[left, right] （这个很重要非常重要）。

区间的定义这就决定了二分法的代码应该如何写，因为定义target在[left, right]区间，所以有如下两点：

while (left <= right) 要使用 <= ，因为left == right是有意义的，所以使用 <=
if (nums[middle] > target) right 要赋值为 middle - 1，因为当前这个nums[middle]一定不是target，那么接下来要查找的左区间结束下标位置就是 middle - 1
"""

def binary_search(num, target):
    left, right = 0, len(num) - 1
    
    while (left <= right):
        #为什么middle要这样写，middle = (left + right)//2
        middle = left + (right - left) // 2
        if num[middle] == target:
            return middle 
        if num[middle] < target:
            left = middle + 1
        elif num[middle] > target:
            right = middle - 1
    return -1

print(binary_search([-1,0,3,5,9,12], 100))

#写法2:左闭右开