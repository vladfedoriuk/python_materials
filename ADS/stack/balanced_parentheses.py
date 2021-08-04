from stack import Stack


def balanced_parentheses(line: str) -> bool:
    stack = Stack()
    balanced = True
    for x in line:
        if x == "(":
            stack.push(x)
        elif x == ")":
            if not stack.empty():
                stack.pop()
            else:
                balanced = False
                return balanced

    if not stack.empty():
        balanced = False
    return balanced


def balanced_general(line: str) -> bool:
    """
    input: '{([])}'
    output: True
    """
    balanced = True
    stack = Stack()
    for s in line:
        if s in ")}]":
            if stack.empty():
                balanced = False
                return balanced
            else:
                if "[{(".find(stack.peek()) == "]})".find(s):
                    stack.pop()
                else:
                    balanced = False
                    return balanced
        elif s in "[{(":
            stack.push(s)

    if not stack.empty():
        balanced = False
    return balanced
