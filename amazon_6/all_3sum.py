# sort and use the same as the traingle finding pythogorean triplets

def all3sum(nums):
    lnums = len(nums)
    if lnums <3 : return []

    result = set()
    nums.sort()

    for i,v in enumerate(nums[:-2]):
        if i!=0 and v == nums[i-1]: # only thing ???????
            continue

        l= i+1
        r = lnums-1
        target = -v

        while l < r:
            if nums[l] + nums[r]==target:
                result.add((v,nums[l], nums[r]))
                l+=1
                r-=1
            elif nums[l] + nums[r] > target:
                r-=1
            else:
                l+=1


    return list(map(list, result))