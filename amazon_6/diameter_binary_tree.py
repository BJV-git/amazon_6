# logic: just need to return the max i.e. height and max sum of the both left height adn right height


def diameter(root):
    val =[0]
    def height(root):
        if not root: return 0
        left_h = height(root.left)
        right_h = height(root.right)
        val[0] =  max(val[0], left_h + right_h)

        return 1+ max(left_h, right_h)

    height(root)

    return val