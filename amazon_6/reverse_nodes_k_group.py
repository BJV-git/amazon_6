# POINT: cross the complete list of k in group, perform the reverse, we know start points to last upnext coming,
# pre then takes start, move curr -> just understand one cycle and repeat

# logic: write the reverse function with limit and repeat it along
# a good practice to create the a dummy node to carry the normal function with out extra case

# Catch: we count for k, and have variables so that cna count on more time
# first move to the k times
# simple loop , pre <- cur, cur<- cur.next, cur.next <- prev
# explained:

# first connect the left to teh right,
# now move the curr to next
# also the first one will be prev so that the upcoming current is pointed

# 123 456 789
# l =1 and r = 4
# first 1 is connected to 4 good
# prev = 1
# cirr = 2

# nwo 2 is connected to 1 and so on



# lastly: new l = r, thne jump = left,
# Else is when the loop breaks

# Time: O(N) - revisit
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reversekgroup(head,k):
    dummy = jump = ListNode(-2)
    dummy.next = l = r = head

    while True:
        count=0
        while r and count < k:
            r = r.next
            count+=1

        if count ==k: # means we found out, with enough length,  that we can invert the list
            pre , cur =r,l
            for _ in range(k): # write the basic logic
                cur.next, cur, pre = pre, cur.next, cur
            jump.next, jump, l = pre, l, r # jump connecting ot new formed list; to the node we need to connect; the next list
        else:
            return dummy.next