# POINT: I need to check for all the elements, check: if len==0, true, out of bounds or != flase, store temp and ret res of all dir
# time: O(MNK), space: O(1)

# may be we can edit matrix and then mark if visited to make sure that directions is not valid

# better can be to use the dfs and while getting back just eliminate things


# Point: to see at every point if dfs works also will make sure that we will not end up in loop, so will remark and again mark back

# catch: zigzag is allowed, only in 4 dir if 8 need to modify at or statement
# bfs: check if curr word matched if so pass rest, so break condition is no word


def check(board,word):
    if not board:
        return False

    board = [list(i) for i in board]
    res=[]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board,i,j,word):
                res.append((i,j))
    return res

def dfs(board,i,j,word):
    if len(word)==0:
        return True
    if i<0 or i >=len(board) or j <0 or j>=len(board[0]) or word[0] != board[i][j]:
        return False
    tmp = board[i][j]
    board[i][j] = '#'

    res = dfs(board,i+1,j,word[1:]) or dfs(board,i-1,j,word[1:]) or dfs(board,i,j+1,word[1:]) or dfs(board,i,j-1,word[1:])
    board[i][j]=tmp

    return res

print(check(["GEEKSFORGEEKS","GEEKSQUIZGEEK","IDEQAPRACTICE"], "EEE"))
