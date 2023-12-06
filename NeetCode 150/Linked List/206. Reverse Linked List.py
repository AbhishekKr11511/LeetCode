'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
'''
def reverse(self, head):
    return head.reverse()

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        newNode = ListNode(val)
        if self.head == None:
            self.head = newNode
            return
        


N = int(input()) # For One line Integer Input

# For an array of intergers in string form separated by a single space
data = [int(x) for x in input().split(' ')]