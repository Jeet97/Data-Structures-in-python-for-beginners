
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def treeContinous(root):
    # Empty tree is always continous.
    if not root:
        return True
    
    # If node is leaf node, return true.
    if not root.left and not root.right:
        return True
    
    # If there's no left node, traverse right node recusively.
    if not root.left:
        return abs(root.data - root.right.data) == 1 and treeContinous(root.right)

     # If there's no right node, traverse left node recusively.
    if not root.right:
        return abs(root.data - root.left.data) == 1 and treeContinous(root.left)

    # If both left and right node are present, traverse both ways.
    return abs(root.data - root.left.data) == 1 and abs(root.data -  root.right.data) == 1 and treeContinous(root.left) and treeContinous(root.right)


if __name__ == '__main__':
    root = newNode(3);
    root.left        = newNode(2)
    root.right       = newNode(4)
    root.left.left  = newNode(1)
    root.left.right = newNode(1)
    root.right.right = newNode(5)

    if treeContinous(root):
        print("yes")
    else:
        print("nope")
