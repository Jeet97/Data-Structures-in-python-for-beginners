from queue import Queue
import time

def reverse(q):
    
    # Return if queue is empty
    if q.empty():
        return
    
    # Dequeue an item from the queue
    x = q.get()

    # Recursive call
    reverse(q)

    # Put the element back to queue
    q.put(x)
    

if __name__ == '__main__':

    try:
        input_arr = [int(x) for x in input('Enter the elements of queue(Space Separated)\n').split()]

        q = Queue()

        for i in range(1, len(input_arr) + 1):
            q.put(i)

        reverse(q)

        for i in range(1, len(input_arr) + 1):
            print(q.get())

    except Exception:
        print("Something went wrong. Please check your input.")
        time.sleep(5)




    




