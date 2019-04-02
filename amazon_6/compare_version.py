# POINT: if exists take else 0 and compare, range in max,
# Time: O(N), space:O(1)



def compare(v1,v2):
    v1 = v1.split('.')
    v2 = v2.split('.')

    v1len = len(v1)
    v2len = len(v2)

    for i in range(max(v1len, v2len)):
        v1 = v1[i] if i < v1len else '0'
        v2 = v2[i] if i < v2len else '0'
        if v1>v2:
            return 1
        elif v2>v1:
            return -1
    return 0