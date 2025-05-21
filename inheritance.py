#Parent class
class dad:
    def __init__(self, eyes, aggresive):
        self.eyes = eyes
        self.aggresive = aggresive

    def display(self):
        print("Your eye color is", self.eyes)
        print("You are aggressive", self.aggresive)

#Child class
class son(dad):
    def __init__(self, name, age, eyes, aggresive):
        self.name = name
        self.age = age

        #invoking the __init__ of parent class
        #to access its attributes
        dad.__init__(self, eyes, aggresive)

#Oject creation
obj = son("Penguin", 8, "blue", True)

#Calling method display
obj.display()

#

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

#

#parent class
class Person(object):
    #__init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

#child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        #invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
    
#creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

#calling a function of the class Person using its instance
a.display()

#

#parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")
    
    def swim(self):
        print("Swim faster")

#child class
class Penguin(Bird):
    def __init__(self):
        #call super() function
        super().__init__()
        print("Penguin is ready")
    
    def whoisThis(self):
        print("Penguin.")

    def run(self):
        print("Run faster")

#Object creation
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()