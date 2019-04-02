# again the logic comes from the DFS, to nullify any found 1's in horizontal or vertical
# increment by 1 and carry on for all

# the nullifier can be done in mltiple ways
# better is to while till we find a zero and stop for that row and column

# need to make sure not stuck in a loop; so defining a direction is better

# works and better: have the possible directions list and recur

def no_of_islands(grid):
    row ,col = len(grid), len(grid[0])
    count=0

    def nullify(r,c):

        possible = [[i,j] for i,j in ([r,c+1], [r,c-1],[r+1,c],[r-1,c]) if 0<=i<row and 0<=j<col]
        # print(r, c, possible)
        for i,j in possible:
            if grid[i][j]=='1':
                grid[i][j]='0'
                nullify(i,j)

    for i in range(row):
        for j in range(col):
            if grid[i][j]=='1':
                # print(i,j)
                grid[i][j]='0'
                count +=1
                nullify(i,j)
    return count

print(no_of_islands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))