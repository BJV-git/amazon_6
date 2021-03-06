# using chaining
class listnode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class hashmap:
    def __init__(self):
        self.m = 1000
        self.h = [None]*self.m

    def put(self, key, value):
        index = key % self.m
        if not self.h[index]:
            self.h[index] = listnode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value)
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = listnode(key, value)

    def get(self, key):
        index  =key%self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next

        return -1

    def remove(self, key):
        index = key % self.m
        cur =prev = self.h[index]
        if not cur: return
        if cur.pair[0] == key: self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur =cur.next
                    prev = prev .next