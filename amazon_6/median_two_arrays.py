
# Time: O(log(M + N))

def median(A,B):
    l = len(A) + len(B)
    if l%2==1:
        return kth(A,B,l//2)
    else:
        return (kth(A,B,l//2) + kth(A,B,l//2-1))/2

def kth(a,b,k):
    if not a:
        return b[k]
    if not b: return a[k]

    ia, ib = len(a)//2

    ma, mb = a[ia], b[ib]

    if k > ia + ib:
        if ma > mb:
            return kth(a, b[ib+1:], k - ib -1 )
        else:
            return kth(a[ia+1:], b, k - ia - 1)

    else:
        if ma > mb:
            kth(a[:ia], b , k)
        else:
            kth(a, b[:ib], k)