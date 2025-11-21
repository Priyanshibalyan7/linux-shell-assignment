class student:
    name="rohan"
    rollno="123"
    def __init__(self,name,marks,roll=345):
        self.name=name
        self.rollno=roll
        self.marks=marks
        def welcome(self):
            print("HELLO")
        def getmarks(self):
            return f"Marks are {self.marks}"

s1=student("rahul", 67,879)
print(s1.name)    
s2=student("arun",80,987)
s2.marks=90
print(s2.marks)


class students:
    def __init__(self ,name,m1,m2,m3,m4):
        self.name=name
        self.marks=[m1,m2,m3,m4]
    def average(self):
        avg=sum(self.marks)/len(self.marks) 
        print(f"average marks of {self.name}: {avg}")
S1=students("vinod",99,98,99,100)
S1.average()






        