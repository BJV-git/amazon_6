
# Time: O(N)
# Space: O(N)
# Logic: just traverse thru all individually

def boundary(root):
    if not root: return []
    if not root.left and not root.right: return [root.val]
    res=[]

    def leaves(root):
        if root:
            leaves(root.left)
            if not root.left and not root.right:
                res.append(root.val)
            leaves(root.right)


    def left(root):
        if root:
            if root.left:
                res.append(root.val)
                left(root.left)
            elif root.right:
                res.append(root.val)
                left(root.right)

    def right(root):
        if root:
            if root.right:
                right(root.right)
                res.append(root.val)
            elif root.left:
                right(root.left)
                res.append(root.val)

    res.append(root.val)
    left(root.left)
    leaves(root.left)
    leaves(root.right)
    right(root.right)

