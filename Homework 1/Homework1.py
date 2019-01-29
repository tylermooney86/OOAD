# Tyler Mooney
# Object Oriented Analysis and Design
# Homework 1 question 4


class Shape:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print("Shape " + str(self.x) + "," + str(self.y) + "," + str(self.z))

class Square(Shape):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print("Square " + str(self.x) + "," + str(self.y) + "," + str(self.z))

class Circle(Shape):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print("Circle " + str(self.x) + "," + str(self.y) + "," + str(self.z))

class Triangle(Shape):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print("Triangle " + str(self.x) + "," + str(self.y) + "," + str(self.z))

class Shapes:
    def __init__(self):
        
        self.shapes = []

    def addShape(self,shape):
        self.shapes.append(shape)

    def sort(self):
        self.shapes = sorted(self.shapes, key=lambda x: x.z, reverse=True)

    def display(self):
        for shape in self.shapes:
            shape.display()
    
    def displayLength(self):
        print("There are " + str(len(self.shapes)) + " shapes in the database.")


## Main ##
if __name__ == "__main__":
    #create shapes for database
    triangle = Triangle(1,1,3)
    square = Square(3,2,1)
    circle = Circle(3,1,2)
    
    #add shapes to database
    shapes = Shapes()
    shapes.addShape(triangle)
    shapes.addShape(square)
    shapes.addShape(circle)

    #display number of shapes in database
    shapes.displayLength()

    #sort and display shapes
    shapes.sort()
    shapes.display()