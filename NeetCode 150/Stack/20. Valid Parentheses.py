'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''
def compare(self, value1, value2):
    return (value1=='(' and value2==')') or (value1=='{' and value2=='}') or (value1=='[' and value2==']')
    
def isValid(self, brackets):
    stack = []
    for i in range(len(brackets)):
        if brackets[i]=='(' or brackets[i]=='{' or brackets[i]=='[':
            stack.append(brackets[i])
        elif brackets[i]==')' or brackets[i]=='}' or brackets[i]==']':
            if len(stack)!=0:
                compareResult = self.compare(stack[-1], brackets[i])
                if compareResult:
                    stack.pop()
                else:
                    return False
            else:
                return False
        else:
            return False
    if len(stack)==0:
        return True
    else:
        return False