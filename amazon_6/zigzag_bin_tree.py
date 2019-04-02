# POINT: have one more variable with dir, and multiply each time

# its just that we need to append the reverse for even ones
# yes so maintain the direction flag and then append as normally

# Time: O(N)
# Space: O(N)

def zigzag_traversal(root):

    if not root: return []
    res,level, direc = [], [root], 1
    while level:
        res.append([n.val for n in level][::direc])
        direc*=-1
        level = [kid for node in level for kid in (node.left , node.right) if kid]
    return res