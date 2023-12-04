'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''

def generateParenthesis(n):
    if n == 0:
        return [""]
    temp = []
    for i in generateParenthesis(n-1):
        combo1 = '(' + i + ')'
        combo2 = '()' + i
        combo3 = i + '()'
        temp.append(combo1)
        temp.append(combo2)
        temp.append(combo3)
    output = set(temp)
    return list(output)


# This question needs back tracking to be solved
def generateParenthesis2(n):
    leftstack = ["("] * n
    rightstack = [")"] * n
    i = 0
    j = 0
    
print(generateParenthesis2(4))
