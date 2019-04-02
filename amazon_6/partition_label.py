# Catch: get the start and end of each digit and sort, and merge
# if we have a start value as 100 means we atleast need to go to 100 to capture this and allow not to fal in others part
# if we face any other one having overlap and greater than the current we merge it, we want a clear split

# Time: O(N)
# Space: O(1)


def partition_label(s):
    if not s : return []
    positions={}

    ls = len(s)
    for i in range(ls):
        if s[i] not in positions:
            positions[s[i]] = [i,i]
        else:
            positions[s[i]][-1] = i

    positions = sorted(positions.values)
    result=[]

    for p in positions:
        start, end = p
        if not (result):
            result.append(p)
        else:
            if result[-1][1] > start:
                result[-1][1] = max(end, result[-1][1])
            else:
                result.append(p)
    return [ (r[1] - r[0])+1 for r in result]