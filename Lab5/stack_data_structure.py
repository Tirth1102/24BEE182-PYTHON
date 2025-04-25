stack = []
while True:
    action = input("Enter action (push/pop/exit): ").lower()
    if action == "push":
        val = input("Enter value to push: ")
        stack.append(val)
    elif action == "pop":
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty")
    elif action == "exit":
        break
    else:
        print("Invalid input")
    print("Current Stack:", stack)
print()

# Output:
# Enter action (push/pop/exit): push
# Enter value to push: 100
# Current Stack: ['100']        
# Enter action (push/pop/exit): pop
# Popped: 100
# Current Stack: []
# Enter action (push/pop/exit): exit