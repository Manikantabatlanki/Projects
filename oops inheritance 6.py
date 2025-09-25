class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        return (self.name,self.age)
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def info(self):
        return (self.name,self.age,self.grade)
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    def info(self):
        return (self.name,self.age,self.subject)
obj1=Person('mani',24)
res=obj1.info()
print(res)

obj2=Student('mani',24,'A')
res=obj2.info()
print(res)

obj3=Teacher('mani',24,'maths')
res=obj3.info()
print(res)
