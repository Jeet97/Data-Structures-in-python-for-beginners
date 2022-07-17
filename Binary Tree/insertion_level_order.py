from queue import Queue

class newNode():
 
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None
         
""" Inorder traversal of a binary tree"""
def inorder(temp):
 
    if (not temp):
        return
 
    inorder(temp.left)
    print(temp.key,end = " ")
    inorder(temp.right)
 
 
"""function to insert element in binary tree """
def insert(temp,key):

    # If tree is empty, insert root and return.
    if not temp:
        root = newNode(key)
        return

    q = Queue()

    q.put(temp)

    while (q.qsize()):
        x = q.get()

        # If a node doesn't have left node, insert new node as left child of that node.
        if (not x.left):
            x.left = newNode(key)
            break

        # If a node has left child, just push the node for further traversal.
        else:
            q.put(x.left)

        # If a node doesn't have right node, insert new node as right child of that node.
        if (not x.right):
            x.right = newNode(key)
            break
        
        # If a node has right child, just push the node for further traversal.
        else:
            q.put(x.right)
   
     
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.left.left = newNode(3)
    root.right = newNode(4)
    root.right.left = newNode(5)
    root.right.right = newNode(6)
 
    print("Inorder traversal before insertion:", end = " ")
    inorder(root)
 
    key = 7
    insert(root, key)
 
    print()
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)
