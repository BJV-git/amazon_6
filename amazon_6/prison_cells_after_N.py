# Catch: seems the pattern repeats once 14 loop is crossed

# Time: O(1)
# Space: O(1)


def prisonafter(cells, N):
    N %= 14
    if N == 0: N = 14
    for i in range(int(N)):
        cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
    return cells

print(prisonafter([0,1,0,1,1,0,0,1], 7))
print(6/14*14)
