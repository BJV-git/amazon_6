# Standard:

# Time: O(N)
# Space: O(N)

def level(self, root):
    if not root: return []
    queue = [root]
    self.res = []
    while queue:
        self.res.append([i.val for i in queue])
        queue = [child for node in queue for child in node.children if child]
    return self.res