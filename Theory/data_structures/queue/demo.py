from collections import deque

# Create a new deque
queue = deque()

# Add elements to the right end
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)  # Output: deque([1, 2, 3])

# Remove and return the leftmost element
left_element = queue.popleft()  # you can use queue.pop() as well
print(left_element)  # Output: 1

# Add an element to the left end
queue.appendleft(4)
print(queue)  # Output: deque([4, 2, 3])
