
def sum3closest(nums, target):
    nums.sort()
    res=sum(nums[:3])
    ln = len(nums)
    for i in range(ln):
        l,r = i+1, ln-1
        while l < r:
            s = sum((nums[i], nums[l], nums[r]))
            if abs(s-target) < abs(res - target):
                res=s
            if s < target:
                l+=1
            elif s > target:
                r-=1
            else:
                return res

    return res