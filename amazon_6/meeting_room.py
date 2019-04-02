# Time: O(nlogn)
# Space: O(1)

# logic: when we add if it comes two we reject so if we find an overlap means False

def possibleallmeet(intervals):
    intervals.sort(key = lambda x: x.start)
    for i in range(len(intervals)):
        if intervals[i].start < intervals[i-1].end:
            return False
    return True