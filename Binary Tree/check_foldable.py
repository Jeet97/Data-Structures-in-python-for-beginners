
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def isFoldable(root):
    if not root:
        return True
    return isSubtreeFoldable(root.left, root.right)

def isSubtreeFoldable(x1, x2):
    
    # If both left and right nodes are not none, return true.
    if not x1 and not x2:
        return True
    # If exactly one of the nodes are empty, then its not a mirror image, return False.
    if not x1 or not x2:
        return False

    # Recursively call opposite node to check for equality and
    # if both subtree are mirror image , return true.
    d1 = isSubtreeFoldable(x1.left, x2.right)
    d2 = isSubtreeFoldable(x1.right, x2.left)

    return d1 and d2

    

if __name__ == "__main__":
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.right = newNode(4)
    root.right.left = newNode(5)
 
    if isFoldable(root):
        print("Tree is foldable")
    else:
        print("Tree is not foldable")
        
