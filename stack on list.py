#stack by using list
class stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,items):
        self.items.append(items)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from the empty stack")
    def peek(self):
       if not self.is_empty():
           return self.items[-1]
       else:
           raise IndexError("pop from the empty stack")
    def size(self): 
        return len(self.items)
stack=stack()
print('is the stack empty',stack.is_empty())
stack.push(1)
stack.push(5)
stack.push(3)
print('stack',stack.items)
print('top of the stack',stack.peek())
print('pop',stack.pop())
print('stack after the pop',stack.items)
print('is the stack is empty',stack.is_empty())
print('size of the stack:',stack.size())