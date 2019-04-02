
# logic: just right left most or right left most

def inordersuc(root, p):
    if p and p.right:
        p = p.right
        while p.left:
            p = p.left
        return p

    suc= None
    while root and root!=p:
        if root.val > p.val: # saving the least greatest value
            suc = root
            root = root.left
        else:
            root = root.right

    return suc