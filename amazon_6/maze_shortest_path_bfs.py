# Point: make use of BFS and visited so that, once we face the min dist, we return
# same as shortest maze logic

# cna actually modify the paths previous problem to make sure the min is returned

# Catch: from each point for the next iter just increment the dist and when ever met return dist
# to avoid loops we use visited matrix else can use set too

# -- better to maintain a list to maintain tuple of points and see rather a matrix

# Time: O(MN)
# Space: O(MN)

def isvalid(maze,x,y):
    if x>=0 and x< len(maze) and y>=0 and y < len(maze) and maze[x][y]==1:
        return True
    return False

def bfs(maze, start, end):
    rows=[-1,0,0,1]
    cols=[0,-1,1,0]

    if not maze[start[0]][start[1]] or not maze[end[0]][end[1]]:
        return -1

    r,c = len(maze), len(maze[0])

    visited=[[False for i in range(c)] for i in range(r)]

    visited[start[0]][start[1]] = True

    queue=[start,0]

    while queue:
        point , dist= queue.pop(0)
        if point == end:
            return dist

        for i in range(4):
            rp = point[0] + rows[i]
            cp = point[1] + cols[i]
            if isvalid(maze,rp, cp) and not visited[rp][cp]:
                visited[rp][cp] = True
                queue.append([[rp, cp], dist+1])
    return -1