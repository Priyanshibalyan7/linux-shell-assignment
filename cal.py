class calculator:
    def add(self, a,b):
        return a+b 
    def subtract(self ,a,b):
        return a-b
    def multiply(self, a,b):
        return a*b
    def divide(self ,a,b):
        if b==0:
            return "error:division by zero is not allowed "
        return a/b 
calc=calculator()
print("addition:",calc.add(10,70))
print("Subtract:",calc.subtract(465-254))
print("multiplication:",calc.mul(58*694))
print("division:", calc.div(985/63))

    
    