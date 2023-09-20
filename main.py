#first a list is made for stack
S = []
#initializations
top = None

#now a func is created to tell if stack is empty or not
def isempty(stk):
    if (stk==[]):
        return True
    else:
        return False

#a func to push is made with "item" as object to be pushed into stack
def push(stk, item):
     stk.append(item) #there, as this is a list the last thing is appended so it works as a stack
     top = len(stk) - 1 #to find top we take length of stack -1

#a func to pop out is made
def pop(stk, item):
    if(isempty(stk)): #checking if stack is not already empty
        return('stack is empty')
    else:
        out = stk.pop
        top = top-1
        return out

#now to display the stack
def display(stk):
    if(isempty(stk)):
        print('stack is empty')
    else:
        top = len(stk) - 1
        print(stk[top], '<--- top')
        for top in range(top-1,-1,-1):
            print(stk(top))

#a while loop to ensure that it goes on until user ends
while True:
 #outputs and inputs
print('Stack Implimentation')
print('1. push')
print('1. pop')
print('1. display')
print('1. exit')
choice=int(input('enter choice'))
#now we work to the stack "s" that we created in the start
if(choice==1):
    item=int(input('enter the item u want to push'))
    push(S,item)
elif(choice==2):
    item=pop(S)
    if(item=='stack is empty'):
        print('underflow')

elif(choice==3):
    display(S)
elif(choice==4):
    break
else:
    print('wrong input')






