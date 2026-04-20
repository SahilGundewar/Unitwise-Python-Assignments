# This program demonstrates error handling when trying to dequeue from an empty queue.

from collections import deque

queue = deque()

def enqueue():
    value = input("Enter value to enqueue: ")
    queue.append(value)
    print("Enqueued:", value)

def safe_dequeue():
    if len(queue) == 0:
        print("Queue is empty, cannot dequeue.")
    else:
        return queue.popleft()


enqueue()
enqueue()

print("Dequeued:", safe_dequeue())
print("Dequeued:", safe_dequeue())
print("Dequeued:", safe_dequeue())  