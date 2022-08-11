#(1)->A class is a collection of objects.
#A class contains the blueprints or the prototype from whichthe objects are created.
#It is a logical entity that contains some attributes and methods..

#(2)
class Calculator:
    def __init__(self):
        print('Welcome')
    def sum(self,x,y):
        return x+y
    def mul(self,x,y):
        return x*y

C=Calculator()
print(C.sum(10,20))
print(C.mul(10,20))

#(10)-> The self always points to the current object.
#(11)-> Abstraction. Encapsulation. Inheritance. Polymorphism.
#(12)->In Python, object-oriented programming (OOPs) is a programming paradigmthat uses objects and classes in programming.
#It aims to implement real entities such as heredity,
#polymorphisms, encapsulation etc. in programming
