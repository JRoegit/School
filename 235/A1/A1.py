# Name: Jacob Roe
# Student Number: 20351389
# I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity.

class Stack:

    global arrsize ##array default size, plus increment amount for resizing
    arrsize = 10

    def __init__(self,arr=[None],topIndex=-1):
        self.arr = [None] * arrsize
        for x in range(len(arr)):
            self.arr[x] = arr[x]
        self.size = arrsize
        self.topIndex = topIndex

    def __str__(self):
        str = ""
        for x in self.arr:
            str += f"[{x}],"
        print(str)
        return str

    def pop(self):
        if self.isEmpty():
            print("String is empty")
            return None
        else:
            top = self.arr[self.topIndex]
            self.topIndex -= 1
            return top

    def push(self,elem):
        self.topIndex += 1
        if self.topIndex == self.size:
            self.expand()
        self.arr[self.topIndex] = elem

    def expand(self):
        self.size = self.size + arrsize
        newArr = [None] * arrsize
        self.arr =  self.arr + newArr

    def isEmpty(self):
        if self.topIndex == -1:
            return True
        else:
            return False

def ex():
    n = 10
    stack = Stack()
    stack.push(n)
    current = n
    while current >= 2:
        current = current//2
        stack.push(current)
    while not stack.isEmpty():
        print(stack.pop())

def f1(n):
    stack = Stack()
    stack.push(n)
    current = n
    while current > 1 :
        if current % 2 == 0:
            current = current//2
            stack.push(current)
        else:
            current = current*3 + 1
            stack.push(current)
    while not stack.isEmpty():
        print(stack.pop())

def f2(n):
    stack = Stack()
    stackleft = Stack() # extra stack
    stack.push(n)
    
    current = n
    while current >= 6:
        current = (current*2)//3
        stack.push(current) 
        if current >= 6:
            stackleft.push(current//3)

    while not stackleft.isEmpty():
        stack.push(stackleft.pop())

    while n >= 6: 
        n = n//3
        stack.push(n)
        while n >= 6:
            n = (n*2)//3
            stack.push((n*2)//3)
            if n >= 6:
                stackleft.push(n//3)
        
    while not stackleft.isEmpty(): #combine stacks
        stack.push(stackleft.pop())
        
    while not stack.isEmpty():
         print(stack.pop())



    # while not stack.isEmpty():
    #     pstack.push(stack.pop())

    # while not pstack.isEmpty():
    #     print(pstack.pop)

def f3(a,b):
    stack = Stack()
    tstack = Stack()
    m = (a+b)//2
    tstack.push((m))
    while a <= m:
        m = ((a+m)//2) - 1
        stack.push(m)
    while m <= b:
        m = ((m+b)//2) + 1
        stack.push(m)

    while not stack.isEmpty():
        print(stack.pop())

def f4(a,b):
    stack = Stack()
    tstack = Stack()
    m = (a+b)//2
    tstack.push((m))
    while a <= m:
        m = ((a+m)//2) - 1
        stack.push(m)
    while m <= b:
        m = ((m+b)//2) + 1
        stack.push(m)

    while not stack.isEmpty():
        print(stack.pop())

def f2r(n):
    if n >= 6:
        f2r(n//3)
        f2r((n*2)//3)
    print(n)

def f3r(a,b):
    if a <= b:
        m = (a+b)//2
        f3r(a,m-1)
        print(m)
        f3r(m+1,b)

def f4r(a,b):
    if a <= b:
        m = (a+b)//2
        f3r(a,m-1)
        f3r(m+1,b)
        print(m)
        

def main():
    
    val1 = [7,18,19,22,105]
    for x in val1 :
        f1(x)

##main()

f2(43)
print("\n")
f2r(43)
        
# f3(1,18)
# print("\n")
# f3r(1,18)


# f4r(1,18)   