

# Simple logic: just use two and move ahead

class ListNode:
    def __init__(self, val):
        pass

def partition(head, x):
    h1 = l1 = ListNode(0)
    h2 = l2 = ListNode(0)

    while head:
        if head.val < x:
            l1.next = head
            l1 =l1.next
        else:
            l2.next = head
            l2 = l2.next
        head = head.next

    l2.next = None
    l1.next = h2.next
    return h1.next