from collections import deque

# stack=deque()

class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def empty(self):
        return len(self.container)==0

    def reverse_string(self,value):
        for char in value:
            self.push(char)

        letters=[]
        while self.size():
            letters.append[self.peek()]
            
        return letters


s=Stack()
s.reverse_string("Nkaka")
print(s.peek())
# s.push("Nkaka")
# s.push(89)
# s.push("Hello")
# print(s.pop())

# print(s.size())























# stack.append("https://nkaka.netlify.com")
# stack.append("www.kigaliToday.com")
# stack.append("www.igihe.com")
# stack.append("www.kwibula.com")
# print("We removed ",stack.pop())
# print(stack)
