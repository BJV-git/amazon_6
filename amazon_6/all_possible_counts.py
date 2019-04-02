# POINT: we are estimating from prev coin all o fo ways + curr index - curr coin and then number of ways the coin can fill up the gap
# downing it to O(N) space: time O(N2)

# is also same as finding the min for each and recursively for the next decreasing count


# doesnt need the coins to be sorted

# Catch: # the no of ways u can get a sum < target is by all the no fo ways already there + the no of ways the curr sum - coin so that
# adding that coin will create those many ways to get the target.
# any where u see no of ways, use a array and adjust into 1 day so that the current is sum of prev + some value


def counts(coins, target):
    lc = len(coins)
    table = [0 for k in range(target+1)]

    table[0]=1

    for i in range(lc):
        for j in range(coins[i], target+1):
            table[j]+=table[j - coins[i]] # its just that he compressed, the prev one to this
        print(table)

    return table[target]


print(counts([2,3,1], 5))