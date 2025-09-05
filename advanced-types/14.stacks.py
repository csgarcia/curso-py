# this corresponds to a stack (LIFO) Last In First Out
# Initializing a stack with some elements

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # Output: [1, 2, 3]
# Popping elements from the stack
print(stack.pop())  # Output: 3
print(stack)
last_element = stack[-1]
print(last_element)  # Output: 2

# check if stack is empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
