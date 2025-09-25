import math
class Shape:
    def area(self):
        pass
    
class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def Area(self):
        return (self.length*self.breadth)

class Circle:
    def __init__(self,r):
        self.radius=r
    def Area(self):
        return math.pi*(self.radius**2)

shapes=[Rectangle(5,3),Circle(4)]
for shape in shapes:
    print(f'Area:{shape.Area():.2f}')
