from queue import Queue

# class to create a node with data, left child and right child.
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
  
# Inorder traversal of a binary tree
def inorder(temp):
    if(not temp):
        return
    inorder(temp.left)
    print(temp.data, end = " ")
    inorder(temp.right)


def deleteDeepest(root, d_node):
    q = Queue()

    q.put(root)

    while (q.qsize()):
        temp = q.get()
        
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.put(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.put(temp.left)


def deleteNode(root, key):
    if not root:
        print('Tree is empty')
        return
    # If root is the only node, return root if same.
    if root.left == None and root.right == None:
        if root.data == key:
            return None
        else:
            return temp
    
    nodeToDelete = None


    q = Queue()

    q.put(root)

    temp = None

    # BFS iteration 
    while (q.qsize()):
        temp = q.get()

        if temp.data == key:
            nodeToDelete = temp

        if temp.left:
            q.put(temp.left)
            
        if temp.right:
            q.put(temp.right)

    if nodeToDelete:
        x = temp.data
        deleteDeepest(root, temp)
        nodeToDelete.data = x

    return root


if __name__=='__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree before the desletion:")
    inorder(root)
    key = 9
    root = deleteNode(root, key)
    print("\n The tree after the deletion;")
    inorder(root)
