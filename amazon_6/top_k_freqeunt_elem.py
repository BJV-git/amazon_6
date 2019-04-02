
# O(N) - Time

def top_k_freq(nums, k):
    hmap={}
    freq={}

    ln = len(nums)
    for i in range(ln):
        hmap[nums[i]] = hmap.get(nums[i],0)+1
    for n, f in hmap.items():
        if f not in freq:
            freq[f] = [n]
        else:
            freq[f].append(n)

    result=[]
    for i in range(ln, 0  , -1):
        if i in freq:
            result.extend(freq[i])
    return result[:k]