# can do it in O(N) with boit manipualtion but can also do in logn

def single(nums):
    lo, hi = 0, len(nums)-1
    while lo < hi:
        mid  = (lo+hi)//2
        if nums[mid] == nums[mid-1]:
            lo = mid+1
        else:
            hi = mid
    return nums[lo]

print(1^1)