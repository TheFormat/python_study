class Calculator :
    
    def __init__(self) :
        self.num1 = 0
        self.num2 = 0
        
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
        
    def pow(self) :
        result = self.num1 ** self.num2
        return result
        
a = int(input())
calc = Calculator()
while True :
    oper = str(input())
    b = int(input())
    calc.setdata(a, b)
    if oper == "+" :
        a = calc.add()
    elif oper == "-" :
        a = calc.sub()
    elif oper == "*" :
        a = calc.mul()
    elif oper == "/" :
        a = calc.div()
    elif oper == "%" :
        a = calc.mod()
    elif oper == "**" :
        a = calc.pow()
    else :
        print("Wrong Operator!")
    print(a)
