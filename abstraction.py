#class square
class square:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("My area is:", self.side**2)

#class circle
class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("My area is:", 3.14*self.radius*self.radius)

#object creation
osquare = square(5)
ocircle = circle(5)

#iterating through objects
for shape in (osquare, ocircle):
    shape.area()

#

#Import necessary modules
from abc import ABC, abstractmethod

#create base class
class Absclass(ABC):
    #Function to print a value
    def print(self,x):
        print("Passed value:", x)
    #Abstract Method
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

#create sub class
class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")

#object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)

#

#import necessary packages
from abc import ABC, abstractmethod
# create a base class
class Animal(ABC):
    #abstract method
    #should be implemented by all sub-classes
    def move(self):
        pass
#sub classes
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
    def move(self):
        print("I can roar")

#Driver code
R = Human()
R.move()

K = Snake()
K.move

R = Dog()
R.move

K = Lion()
K.move