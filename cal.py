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
print("subtraction:",calc.subtract(90,50))
print("multiplication:",calc.multiply(5,6)) 


    
    