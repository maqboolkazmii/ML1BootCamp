import numpy as np
stack = np.zeros(10)
index = 0
for i in range(50):
    options = input("Enter Option 1.pop, 2.push, 3.exit: ")
    if options == "push":
        if index < 10:
            number = int(input("Enter number that you want to add in stack: "))
            print(number)
            stack[index] = number
            print(stack)
            index += 1
            print("Index is -----", index)
        else:
            index >= 10
            print("Stack is full")
        
    if options == "pop":
        if index == 0:
            print("Stack is empty")
        else:
            stack[index-1] = 0
            print(stack)
            index -= 1
    if options == "exit":
        break
