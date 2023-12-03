'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''

class MinStack(object):

    minimum = []
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        if len(self.minimum) == 0:
            self.minimum.append(val)
        elif self.minimum[-1] > val:
            self.minimum.append(val)
        return None

    def pop(self):
        if self.minimum[-1] == self.stack.pop():
            self.stack.pop()
            self.minimum.pop()
        else:
            self.stack.pop()
        return None
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minimum[-1]
    
    def display(self):
        return self.stack


myStack = MinStack()
print(myStack.push(-2))
print(myStack.push(0))
print(myStack.push(-3))
print(myStack.display())
print(myStack.getMin())
print(myStack.pop())
print(myStack.display())
print(myStack.top())
print(myStack.getMin())

