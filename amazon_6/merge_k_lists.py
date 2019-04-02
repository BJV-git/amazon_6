# POINT: have a priority queue, if set as next, see if it has next to get and put in PQ

# Catch: the algorithm for the infinite large sort, have a proority queue which sorts all divisions and outpouts
# in q first put all first nodes
# also have the new one getting formed and before put just check

# Time: O(MN)
# Space: O(MN)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from queue import PriorityQueue

def merge_k_lists(lists):
    dummy =ListNode(None)
    curr=dummy

    p=PriorityQueue()

    for node in lists: # just inserting the starting node and that's it caz we cna iterate using next
        if node: p.put((node.val, node))

    while p.qsize()>0:
        curr.next = p.get()[1]
        curr=curr.next
        if curr.next: p.put((curr.next.val, curr.next)) # adding the next node to the priority queue so we are having only the three things in
                                                        # pq and trying to get the best while adding the new one

    return dummy.next