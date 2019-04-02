# POINT: for k smallest, we are pushing with -d, so now we push normal, instead of pushpop just replace

# the idea is to maintain the length of k, and then if some thing new comes just see the value to replace

# Catch min heap and maintain those k largest elements

# TIME: O(K) form heap, pop - O(logk) to readjust
# SPace: O(k)

import  heapq

class Kthlargest(object):
    def __init__(self, k, nums):
        self.nums = nums
        self.k =k

        heapq.heapify(self.nums)

        while len(self.nums) > self.k: # making sure we have the length i.e. the largest k elements so if popped will get
            heapq.heappop(self.nums)   #

    def add(self,n):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, n)
        else:
            heapq.heapreplace(self.nums, n)
        return self.nums[0]
    def popp(self):
        heapq.heappop(self.nums)