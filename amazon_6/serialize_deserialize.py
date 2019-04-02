# POINT: get it in pre order, so while forming, node = val, .left = decode and .right = decode

#Catch: serialize: pre order if not root append '#'
# deserialize: first as its pre order we need to do left and right,

# Serialize: Time: O(N), Space: O(N)
# deSerialize: Time: O(N), Space: O(N)

class Treenode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class codec:

    def serialize(self, root):
        def encode(root):
            if root:
                val.append(root.val) # pre order
                encode(root.left)
                encode(root.right)
            else:
                val.append('#')
        val=[]
        encode(root)
        return ''.join(val)

    def deserialize(self,data):

        def decode():
            value = next(val)
            if val=='#':
                return None
            node = Treenode(int(val))
            node.left = decode()
            node.right = decode()
            return node
        val = iter(data.split())
        return decode
