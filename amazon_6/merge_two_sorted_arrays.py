# POINT: expanding the array on the end side, start from last, if a> means all n fit before it else other one

# logic: if the largest of one is > other then we need to any ways accommodate the n extra space
# so will follow the same rule

# teh reason in coming from last is that no need to move all teh next elements to right and then again re arranage

# Catch: we extend the array so repeat while there exist the other count
# Time: O(M+N)
# Space : O(min())


def merge_two(a,m,b,n):
    while n:
        if m and a[m-1] >= b[n-1]:
            a[m+n-1] = a[m-1]
            m-=1
        else:
            a[m + n - 1] = b[n - 1]
            n -= 1