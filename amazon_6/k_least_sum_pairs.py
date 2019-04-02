
# same logic as if how we sort infinite no of files so just take advantage of the graph structure as they are in sorted order
# we can also use priority queue but we need numbers so need the indices matrix

# Time: O(mLog H)

# Logic: form a graph as they are in increasing order and traverse through it
import heapq
def ksmallest(nums1, nums2, k):
    res=[]
    lnums2 = len(nums2)
    lnums1 = len(nums1)
    queue = [(nums1[0] + nums2[0],(0,0))]
    visited=set()
    while len(res) < k and queue:
        _, (i,j) = heapq.heappop(queue)
        res.append((nums1[i], nums2[j]))

        if j+1 < lnums2 and (i, j+1) not in visited:
            heapq.heappush(queue, (nums1[i] + nums2[j+1], (i, j+1)))
            visited.add((i, j+1))
        if i+1 < lnums1 and (i+1, j) not in visited:
            heapq.heappush(queue, (nums1[i+1] + nums2[j], (i+1, j )))
            visited.add((i+1, j ))
    return res