import sys
import time

class StackQueue:
    
    def __init__(self, size):
        self.arr = []
        self.size = size
    # To check if queue is empty
    def isEmpty(self):
        return len(self.arr) == 0
    
    # To check if queue is full
    def isFull(self):
        return len(self.arr) == self.size


    # Enqueue an item to the queue 
    def enqueue(self, data):
        if self.isFull():
            print('Queue is full')
            return

        self.arr.append(data)

    # Dequeue an item from the queue
    def dequeue(self):
        # Return if queue is empty
        if self.isEmpty():
            print('Queue is Empty')
            return

        # pop an item from the stack
        x = self.arr.pop()

        # if stack become empty
        # return the popped item
        if self.isEmpty():
            return x
        
        # recursive call
        n = self.dequeue()

        # push popped item back to
        # the stack
        self.arr.append(x)

        # return the result of 
        # deQueue() call
        return n


if __name__ == '__main__':

    try:
        input_arr = [int(x) for x in input('Enter the elements of queue(Space Separated)\n').split()]

        q = StackQueue(len(input_arr))

        for i in input_arr:
            q.enqueue(i)

        print('Trying to enqueue 7 ...')
        
        # Will cause stack overflow
        q.enqueue(7)

        for i in input_arr:
            print(q.dequeue())

        print('Trying to dequeue again..')
        
        # Will cause stack underflow
        q.dequeue()

    except Exception:
        print("Something went wrong. Please check your input.")
        time.sleep(5)
