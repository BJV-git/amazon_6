# logic: just use the heap
import heapq

def kth_largest(nums,k):
    arr = nums[:k]
    heapq.heapify(arr)
    for num in nums[k:]:
        if num > arr[0]:
            heapq.heapreplace(arr, num)
    return arr[0]