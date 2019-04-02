# Catch: just play the game, make sure u go in opposite direction based on the zigzag

# Time: O(N)
# Space: O(N)

def snakeladder(board):
    n = len(board)
    need = {1:0}
    bfs=[1]
    for position in bfs:
        for i in range(position+1, position+7):
            row, column = (i-1)/n, (i-1)%n
            next_position = board[~row][column if row%2==0 else ~column]
            if next_position > 0 : i = next_position # climbing the ladder of downing for the snake
            if i== n*n : return need[position] +1
            if i not in need:
                need[i] = need[position]+1
                bfs.append(i)
    return -1