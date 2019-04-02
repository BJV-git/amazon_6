# logic: same as the merge intervals, but differs based on the application.
# all we are looking is before its gets to zero is any comes in between way, as before -1 if somehting comes means
# we need to look for a room

# Time: O(NlogN)
# Space: O(N)


class interval(object):
    def __init__(self,s=0,e=0):
        self.start = s
        self.end = e

class solution(object):
    def meetroomsmin(self, intervals):
        if not intervals: return  0
        timeline=[]
        for i in intervals:
            timeline.append((i[0], 1))
            timeline.append((i[1],-1))
        timeline.sort()
        print(timeline)

        ans = curr=0
        for _, v in timeline:
            curr+=v
            ans = max(ans,curr)
        return ans

s = solution()
print(s.meetroomsmin([[0,30],[5,10],[15,20]]))