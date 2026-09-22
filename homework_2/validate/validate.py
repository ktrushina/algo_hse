def validate(pushed, popped):
    stack = []
    counter = 0

    for value in pushed:
        stack.append(value)

        while stack and counter < len(popped) and stack[-1] == popped[counter]:
            stack.pop()
            counter += 1

    return counter == len(popped)

'''
или с помощью реализованного ранее stack

from stack import Stack 

def validate(pushed, popped):
    stack = Stack()         
    counter = 0

    for value in pushed:
        stack.push(value)    # push вместо append

        while not stack.is_empty() and counter < len(popped) and stack.peek() == popped[counter]:
            stack.pop()
            counter+= 1

    return counter == len(popped)
'''    
