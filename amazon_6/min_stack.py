# Logic: just attach the min to each element as tuple so can have record at that point of time what is the minimum

# Time: O(1)
# Space: O(N)

class minstack:
    def __init__(self):
        self.q = []

    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    def pop(self):
        self.q.pop()

    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][0]

    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][1]