# Valid Parentheses - 5kyu
# write a function that takes a string of parentheses, and determines if the order of parentheses is valid. the function should return true if valid, false if not

def valid_parentheses(string):
    stack = []
    if len(string) == 0:
        return True
    for element in string:
        if element == '(':
            stack.append(element)
        elif element == ')' and len(stack) > 0:
            stack.pop()
        elif element == ')' and len(stack) == 0:
            return False
    if len(stack) > 0:
        return False
    else: 
        return True
    
valid_parentheses("  (")
valid_parentheses(")test")
valid_parentheses("")
valid_parentheses("hi())(")
valid_parentheses("hi(hi)()")


