queue = []
while True:
    action = input("Enter action (enqueue/dequeue/exit): ").lower()
    if action == "enqueue":
        val = input("Enter value to enqueue: ")
        queue.append(val)
    elif action == "dequeue":
        if queue:
            print("Dequeued:", queue.pop(0))
        else:
            print("Queue is empty")
    elif action == "exit":
        break
    else:
        print("Invalid input")
    print("Current Queue:", queue)
print()

# Output:
# Enter action (enqueue/dequeue/exit): enqueue
# Enter value to enqueue: 1000
# Current Queue: ['1000']
# Enter action (enqueue/dequeue/exit): exit