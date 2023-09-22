# global variables and stack
stack = [None for i in range(6)]
null = -1
top = null

def init_stack():
    global top
    for i in range(6):
        stack[i] = None
    top = null

# push. description: push a value into the stack
def push(data):
    global top, stack
    if top == len(stack) - 1:
        print("Stack Overflow")
    else:
        top += 1
        stack[top] = data

# pop. description: pop a value from the stack
def pop():
    global top, stack
    if top == null:
        print("Stack Underflow")
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data

# display. description: display the stack and
# the top of the stack pointer as arrow in vertical order
def display():
    global top, stack
    if top == null:
        print("Stack is empty")
    else:
        for i in range(len(stack)-1, null, -1):
            if i == top:
                print(stack[i], "\t<--- top")
            else:
                print(stack[i])

# main menu
choice = 0
while choice != 5:
    print("\nStack Menu\n")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Initialize Stack")
    print("5. Quit")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        data = input("Enter data: ")
        push(data)
    elif choice == 2:
        data = pop()
        print("Data popped => ", data)
    elif choice == 3:
        display()
    elif choice == 4:
        init_stack()
    elif choice == 5:
         print("Exiting...")
    else:
        print("Invalid choice!!")