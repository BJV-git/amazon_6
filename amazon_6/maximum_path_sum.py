# point: just go through all the elem, and at each = max(previous 3 possible elem connections
# time: O(MN), space: O(1)

#for each element just take the max u can so just like the coin based and move on just
# keep the max value updated all time

def max_path(M):
    r,c = len(M), len(M[0])

    res=-1

    for i in range(1,r):
        for j in range(c):
            if j>0 and j < c-1:
                M[i][j] += max( M[i-1][j] , max(M[i-1][j-1], M[i-1][j+1]))
            elif j>0:
                M[i][j] += max(M[i-1][j-1], M[i-1][j])
            elif j < c-1:
                M[i][j] += max(M[i-1][j+1], M[i-1][j])

            res = max(M[i][j], res)

    return res

print(max_path([[ 0, 10, 2, 0, 200, 4 ],
                [ 1000, 0, 100, 0, 2, 5 ],
                [ 0, 10, 4, 0, 2, 0 ],
                [ 1, 0, 2, 20, 0, 4 ]]))