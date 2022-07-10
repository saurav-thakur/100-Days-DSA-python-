def sort_a_stack(stack):

    if len(stack) == 0:
        return

    num = stack.pop()
    sort_a_stack(stack)

    sort_recursively(stack,num)

    return stack

def sort_recursively(stack,num):

    if len(stack) == 0 or stack[-1] < num:
        stack.append(num)
        return

    n = stack.pop()
    sort_recursively(stack,num)

    stack.append(n)

    return stack

stack = [2,4,1,3,5,6,9,7]
print(sort_a_stack(stack))