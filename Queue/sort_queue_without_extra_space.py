from queue import Queue


def sortQueue(queue):
    for i in range(1, queue.qsize() + 1):
        # First find the next minimum node in the queue(only upto the already sorted index)
        minIndex = findMinIndex(queue, queue.qsize() - i)
        # Insert min value at the end of the queue.
        enqueueMinIndex(queue, minIndex)

def findMinIndex(queue, sortedIndex):
    minIndex = -1
    minValue = 999999999

    # Only iterate upto already sorted part of the queue.
    for i in range(q.qsize()):
        curr = queue.get()

        # If current element is less than or equal to minValue and current index is less than or equal to
        # sorted index, assign current index as min index.
        if minValue >= curr and i <= sortedIndex:
            minIndex = i
            minValue = curr
        queue.put(curr)
        
    return minIndex


def enqueueMinIndex(queue, minIndex):
    minValue = None
    for i in range(queue.qsize()):
        curr = queue.get()

        # If current index is not equal to min index, put the item back to the queue.
        if i != minIndex:
            queue.put(curr)
        # If current index is equal to min index, assign current value as min value.
        else:
            minValue = curr

    queue.put(minValue)



if __name__ == '__main__':

    try:
        input_arr = [int(x) for x in input('Enter the elements of queue(Space Separated)\n').split()]

        q = Queue()

        for i in input_arr:
            q.put(i)

        sortQueue(q)

        for i in range(1, len(input_arr) + 1):
            print(q.get())

    except Exception:
        print("Something went wrong. Please check your input.")
        time.sleep(5)
