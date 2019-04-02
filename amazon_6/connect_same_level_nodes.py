# Point: make a connection to move right or left, store next at initial and carry on

# can use level order wed know and simply take the list to connect the rights consecutively

#learned logic: from top we will setup the next xonnextion so we can usethat to traverse to the next all childs

# Catch: when at root connect the childs, and use the connection move in next level and so on
# first store the next left and then start the process
# make two conditional connections and move on

# Time: O(N)
# Space : O(1)

def connect_same_level_nodes(root):
    while root and root.left:
        next = root.left
        while root:
            root.left.next = root.right
            root.right.next = root.next and root.next.left
            root = root.next
        root = next