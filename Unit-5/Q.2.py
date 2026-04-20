# This program demonstrates error handling when trying to pop from an empty stack.

stack = []

def push():
    value = input("Enter value to push: ")
    stack.append(value)
    print("Pushed:", value)

def safe_pop():
    if len(stack) == 0:
        print("Stack is empty, nothing to pop.")
        return None
    else:
        return stack.pop()


push()
push()

print("Popped:", safe_pop())
print("Popped:", safe_pop())
print("Popped:", safe_pop())  