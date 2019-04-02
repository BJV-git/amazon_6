# common logic
# Time: O(N log N)

def meregintervals(intervals):
    out=[]
    for i in sorted(intervals, key = lambda i: i[0]):
        if out and i[0] <= out[-1][1]:
            out[-1][1] = max(i[1],out[-1][1] )
        else:
            out += i
    return out


# out = []
#     for i in sorted(intervals, key=lambda i: i.start):
#         if out and i.start <= out[-1].end:
#             out[-1].end = max(out[-1].end, i.end)
#         else:
#             out += i,
#     return out