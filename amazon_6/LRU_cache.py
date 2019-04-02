# POINT: use dll, dict to see if we have key and if so remove, so no time taken in doing so.
# if get, remove and add: put, node and key knows each other, for in del
# how the dic and ll is updated

# Catch: simple how LRU works, if new called oer exist call, we have to remove or add at start so dll is the best
# to remove we need to have a dic(key) storing the node (key, val)


# Time: O(1) - over all O(N)
# Space: O(N)

class Node(object):
    def __init__(self,k,v):
        self.key = k
        self.val = v
        self.prev=None
        self.next = None

class LRUCache(object):
    def __init__(self,capacity):
        self.cap = capacity
        self.dic = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self,key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add_at_end(n)
            return n.val
        return -1

    def put(self,key,value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add_at_end(n)
        self.dic[key] = n
        if len(self.dic) > self.cap: # we will remove the first one i.e. from the head
            n  = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self,node): # normal removing and adding the nodes
        p = node.prev # storing the both left and right and assigning to remove
        n = node.next
        p.next = n
        n.prev=p

    def _add_at_end(self,node):
        p = self.tail.prev # storing the tail prev and then all addings are new
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

