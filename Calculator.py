class Calculator :
    
    def __init__(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2
        
    def setdata(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2
        
    def add(self) :
        result = self.num1 + self.num2
        return result
        
    def sub(self) :
        result = self.num1 - self.num2
        return result
        
    def mul(self) :
        result = self.num1 * self.num2
        return result
        
    def div(self) :
        result = self.num1 / self.num2
        return result
        
    def mod(self) :
        result = self.num1 % self.num2
        return result
        
a = int(input())
c = str(input())
b = int(input())
f = Calculator(a, b)
while True :
    r = int()
    if c == "add" :
        f.setdata(a, b)
        r = f.add()
    elif c == "sub" :
        f.setdata(a, b)
        r = f.sub()
    elif c == "mul" :
        f.setdata(a, b)
        r = f.mul()
    elif c == "div" :
        f.setdata(a, b)
        r = f.div()
    elif c == "mod" :
        f.setdata(a, b)
        r = f.mod()
    else :
        print("Wrong Operator!")
    print(r)
