"""
## Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
and this is the only possible move.  The result of this move is that the string is "aaca", 
of which only "aa" is possible, so the final string is "ca".

## Example 2:
Input: s = "azxxzy"
Output: "ay"

"""

class Stack:
    stack = []
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[len(self.stack)]
        else:
            return '-1'

    def pop(self):
        if self.stack != []:
            self.stack.pop()

    def get_str(self):
        str = ""
        for x in self.stack:
            str += x
        return str

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = Stack()
        for x in s:
            if stk.peek() != x or stk.peek() == '-1':
                stk.push(x)
            else:
                stk.pop()

        str = stk.get_str()
        return str

class Stack:
    stack = []
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def peek(self):
        if self.stack != []:
            return self.stack[len(self.stack)-1]
        else:
            return '-1'

    def pop(self):
        if self.stack != []:
            self.stack.pop()

    def get_str(self):
        str = ""
        for x in self.stack:
            str += x
        return str

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = Stack()
        for x in s:
            if stk.peek() == '-1':
                stk.push(x)
            else:
                if stk.peek() != x:
                    stk.push(x)
                else:    
                    stk.pop()

        str = stk.get_str()
        return str
