# need to find the min steps needed for the end reach

def jump(nums):
    ln = len(nums)
    if ln < 2: return 0
    l,r = 0, nums[0]
    times=1

    while r < ln-1:
        times+=1
        next = max(i+nums[i] for i in range(l, r+1))
        l, r = r, next
        print(l,r)
    return times

print(jump([2,3,1,1,4]))