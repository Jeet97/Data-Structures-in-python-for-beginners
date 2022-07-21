

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def height(root):
        
    if not root:
        return 0

    # Initialize height as 1 for every node.
    c1 = 1
    c2 = 1

    # If left subtree is present, continue iterating and add 1 each time.
    if root.left:
        c1 = 1 + height(root.left)

    # If right subtree is present, continue iterating and add 1 each time.
    if root.right:
        c2 = 1 + height(root.right)
    
    # If left subtree is greater than right subtree, return height of left subtree
    # other return height of right subtree 
    return  c1 if c1 > c2 else c2


if __name__ == '__main__':
    root = newNode(3);
    root.left        = newNode(2)
    root.right       = newNode(4)
    root.left.left  = newNode(1)
    root.left.right = newNode(1)
    root.left.right.left = newNode(1)
    root.right.right = newNode(5)

    print(height(root))
