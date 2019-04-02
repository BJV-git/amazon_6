# logic: so while changing the state of the current element we should do in such a way that it can be traced while changing for upcoming

def gameOfLife( board):
    rows, cols = len(board), len(board[0])

    for i in range(rows):
        for j in range(cols):
            # print("row and column", i, j)

            neighbours = [(i+1,j+1),(i,j+1),(i+1,j),(i-1,j-1),(i-1,j),(i,j-1),(i+1,j-1),(i-1,j+1)]
            # print("neighbours are", neighbours)
            possible_neighbours = [(i,j) for i,j in neighbours if 0<=i<rows and 0<=j<cols]
            # print("possible neighbours are", possible_neighbours)
            status=[board[i][j] for i,j in possible_neighbours]
            no_of_pos = sum((i==1 or i==-1) for i in status)
            no_of_neg = sum((i==0 or i==2)for i in status)

            if board[i][j] == 0 and (no_of_pos==3):
                board[i][j]=2
            elif board[i][j]==1 and ( not(no_of_pos ==2 or no_of_pos==3)) :
                board[i][j] = -1
    # print(board)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] <= 0:
                board[i][j] =0
            elif board[i][j] > 0:
                board[i][j]=1

    print(board)

gameOfLife([[0,0,0]])