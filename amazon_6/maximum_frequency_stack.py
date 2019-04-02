
# Time: O(1)
# Space: O(N)

# Catch: maintain freq each with counter, for each freq mainatin the numbers with dic
# can pop in the order they are the frequencies

import collections
class FreqStack(object):
    def __init__(self):
        self.freq = collections.Counter()
        self.m = collections.defaultdict(list)
        self.maxf = 0

    def push(self, x):
        self.freq[x] += 1
        self.maxf = max(self.maxf, self.freq[x])
        self.m[self.freq[x]].append(x)

    def pop(self):
        x = self.m[self.maxf].pop()
        if not self.m[self.maxf]: self.maxf -= 1
        self.freq[x] -= 1
        return x
