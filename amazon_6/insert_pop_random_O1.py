import random
class sol:
    def __init__(self):
        self.nums=[]
        self.pos={}
        self.len=0

    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = self.len
            self.len+=1
            return True
        return False

    def remove(self, val): # we exchange the last and has to be removed and do it in O(1)
        if val in self.pos:
            ind, last = self.pos[val], self.nums[-1]
            self.nums[ind], self.pos[last] = last, ind
            self.nums.pop()
            self.pos.pop(val,0)
            self.len-=1
            return True
        return False

    def getRandom(self):
        return self.nums[random.randint(0, self.len -1)]