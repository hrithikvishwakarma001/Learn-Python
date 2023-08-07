
# Implement Stack using Queue: Use Python's queue data structure to implement a stack.
# - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
# Output: "1, None, 3, None, None"

from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue = Queue()

    def push(self, value):
        self.queue.put(value)

    def pop(self):
        if self.queue.empty():
            return None

        size = self.queue.qsize()
        for _ in range(size - 1):
            self.queue.put(self.queue.get())

        return self.queue.get()

stack = StackUsingQueue()
output = []

stack.push(1)
output.append(stack.pop())

stack.push(2)
output.append(stack.pop())

stack.push(3)
output.append(stack.pop())
output.append(stack.pop())

print(", ".join(str(val) for val in output))
