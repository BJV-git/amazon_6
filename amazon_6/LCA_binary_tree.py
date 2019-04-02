# POINT: check and flag is the base case, return root if both or else

# using the prev logic; if left and right has then set the flag and move on

# Catch: three cases, either root, left or right
# we know at every point we check this recursively
# so return if both then root else either

# Time: O(N)
# Space: O(1)

def lcabinarytree(root,p,q):

    if root in (None,p,q): return root # condition for same
    left = lcabinarytree(root.left,p,q)
    right = lcabinarytree(root.right,p,q)
    return root if left and right else left or right