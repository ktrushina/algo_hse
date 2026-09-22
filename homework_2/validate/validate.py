def validate(pushed, popped):
    stack = []
    matched = 0

    for value in pushed:
        stack.append(value)

        while stack and matched < len(popped) and stack[-1] == popped[matched]:
            stack.pop()
            matched += 1

    return matched == len(popped)

'''
или с помощью реализованного ранее stack (homework_2/stack_vs_queue/stack.py)

from stack import Stack 

def validate(pushed, popped):
    stack = Stack()         
    matched = 0

    for value in pushed:
        stack.push(value)    # push вместо append

        while not stack.is_empty() and matched < len(popped) and stack.peek() == popped[matched]:
            stack.pop()
            matched+= 1

    return matched == len(popped)
'''    
