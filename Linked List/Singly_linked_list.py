class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:


    def __init__(self):
        self.head = None


    def traverse(self):
        temp = self.head

        while temp:
            print (temp.data)
            temp = temp.next


    def insertAtBegining(self, node):
        newNode = node
        newNode.next = self.head
        self.head = newNode

        
    


if __name__ == '__main__':


    # Creation
    
    ll = LinkedList()

    ll.head = Node(1)    # Creating new node and assigning it to head.
    second = Node(2)
    third = Node(3)

    ll.head.next = second  # Updating next reference of head node to point to second node.
    second.next = third

    # Insertion

    first =  Node(0)
    ll.insertAtBegining(first)


    # Traversing
    
    ll.traverse()
