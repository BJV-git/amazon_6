# logic: inspired from bfs of min perfect sum of n - but from opposite direction i.e. the add up that is - and see if meets coin

# simple, just form the array whose sums are less than the amount and in the iteration just if found return count

# but some times, the sum might repeat so need to use the visited, simple

# catch: go reverse i.e from 0 and make sure no same sum again visiting
# Time: O(N)  -- as the amount may be by 1 in worst case
# Space: O(N) -- as the amount may be by 1 in worst case

def bfs_min_coins(coins, amount):
    if not amount: return amount

    value1=[0]
    value=[]

    count=0
    visited = set()

    while value1:
        count+=1
        for v in value1:
            for coin in coins:
                val = coin + v
                if val==amount:
                    return count
                elif val > amount:
                    continue
                elif val not in  visited:
                    visited.add(val)
                    value.append(val)

        value1, value = value, []
    return -1

print(bfs_min_coins([235,326,180,11,61,483,464,125,403,241],5926))