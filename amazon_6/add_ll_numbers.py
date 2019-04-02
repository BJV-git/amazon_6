# simple: add and carry the other stuff to next node


# Catch: we need to get the carry and move to next to add,
# so use divmod (both values + carry) with 10 and apend to the next node and move on


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addll(l1,l2):
    carry=0
    root =  n = ListNode(0)

    while l1 or l2 or carry:
        v1=v2=0 # for storing the values of two nodes
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next