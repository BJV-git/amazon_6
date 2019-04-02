# for half I believe will use three pointers, slow and fast, prev and do the job

# Catch: can also use the logic of the palindrome
# just that making sure we stop at the end of first half, jsut have fast start as head.next to stop slow before half

# Time: O(N)
# Space: O(1)

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next=None

# will start when m is met and will continue till n lasts or the list ends

def reverse(head,m,n):
    def reverse(head, ite): # here the ite is the number of right links we shift to left
        prev = None
        curr = head
        next = None
        while curr  and ite:
            next = curr.next  # like normal operation as we shift the next but we save it before
            curr.next = prev  # set it
            prev = curr  # shift
            curr = next
            ite -= 1

        return prev, next

    t_head = head

    if m > 1:
        while m > 2:
            head = head.next
            m -= 1
        print(head.val)
        temp = head.next
        head.next, temp.next = reverse(head.next, n - m)

        return t_head
    else:
        temp = head
        ret, temp.next = reverse(head, n)
        return ret