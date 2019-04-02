# logic: form a graph, then start from node and mark -1 and the connected nodes as 1
# repeat and so on

# common dfs strategy - we set the current to -1 or any other thing, after dfs at current we again reset it

# we want to do dfs, but how? ; go for each course, but for each I need prereqs so form graph
# , remember -1,1 0 strategy, form visited

# Time: O(V+E)
# Space: O(V+E)

def canfinish(numCourses, prereqs):
    graph = [[] for _ in range(numCourses)]
    vis = [0 for _ in range(numCourses)]

    for x,y in prereqs:
        graph[x].append(y)

    def dfs(i):
        if vis[i]==-1:
            return  False
        if vis[i] == 1: # lets say we have B for which we need to do D and we checked B to be all good, now for C we need ot do
            return True # B again no need to repeating the entire process so will mark as 1 so that no need of extra process

        vis[i] = -1

        for prqs in graph[i]:
            if not dfs(prqs):
                return False

        vis[i] = 1
        return True

    for i in range(numCourses):  # so we start with course 0 , like mimicing the random initialization
                                 # i.e. 0 might not be a start point
        if not dfs(i):
            return False
    return True