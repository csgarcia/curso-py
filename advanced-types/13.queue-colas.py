from collections import deque

# this correspondes to a queue (FIFO)
# Initializing a queue with some elements

rows = deque([1, 2, 3, 4, 5])
print(rows)  # Output: deque([1, 2, 3, 4, 5])
# Adding an element to the end of the queue
rows.append(6)
rows.append(7)
print(rows)  # Output: deque([1, 2, 3, 4, 5, 6, 7])

# Removing an element from the front of the queue
rows.popleft()
print(rows)  # Output: deque([2, 3, 4, 5, 6, 7])

if not rows:
    print("Queue is empty")  # Output: Queue is empty
