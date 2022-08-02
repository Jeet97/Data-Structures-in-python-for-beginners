
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def isSumProperty(root):
    # If current element is null, return true.
    if not root:
        return 1
        
    d1 = 0
    d2 = 0
        
    if root.left:
        d1 = root.left.data
        
    if root.right:
        d2 = root.right.data

    # If sum of value of child nodes is not equal to parent node value, and current node is not
    # a leaf node, return false.
    if root.data != d1 + d2 and (d1 or d2):
        return 0

    # Recursively check for left and right subtree.
    return isSumProperty(root.left) and isSumProperty(root.right)


if __name__ == '__main__':
    root = newNode(10);
    root.left        = newNode(5)
    root.right       = newNode(5)
    root.left.left  = newNode(1)
    root.left.right = newNode(4)
    root.right.right = newNode(1)

    if isSumProperty(root):
        print("yes")
    else:
        print("nope")
