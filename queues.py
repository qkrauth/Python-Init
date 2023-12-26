# Queues are FIFO - First in First out

from collections import deque

# Deque

data = deque()
data.append("Quinten")
element = data.popleft() # popleft returns the left-most item (First)

print(element, data)