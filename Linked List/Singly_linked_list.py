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

    def insertAtEnd(self, node):
        newNode = node
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newNode

    def insertAtMiddle(self, node, position):

        newNode = node
        count = 1
        temp = self.head

        while count != position-1:
            count+=1
            temp = temp.next

        newNode.next = temp.next
        temp.next = newNode



    def deletionAtBegining(self):
        self.head = self.head.next

    def deletionAtMiddle(self, position):
        temp = self.head
        count = 0

        while count != position - 1:
            temp = temp.next
            count+=1


        temp.next = temp.next.next
    


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
    fourth = Node(4)
    ll.insertAtEnd(fourth)
    middleNode = Node(2.5)
    ll.insertAtMiddle(middleNode, 4)

    ll.traverse()


    # Deletion

    ll.deletionAtBegining()
    ll.deletionAtMiddle(3)


    # Traversing
    
    ll.traverse()
