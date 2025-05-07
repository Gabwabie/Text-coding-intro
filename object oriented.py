class person:
    #class variable
    legs = 2
    head = 1
    hands = 2

    #instance variables
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
#instance of the class
p1 = person("Gabby",14,1.5)
p2 = person("Danstan",27,2.2)

print(p1.name)
print(p2.age)

#Student Class

#create a class
class student:
    grade = 10
    print("Hi I am a student of grade", grade)
#create an object
ob = student()

#Vehicle Class

#create a class
class Vehicle:
    #create init method
    def __init__(self,max_speed,mileage):
        #bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage
#Object creation
modelX = Vehicle(240,18)

#access the varaibles inside init method
print("Model Max Speed:",modelX.max_speed)
print("Model Mileage:", modelX.mileage)

#Parrot Class

class Parrot:
    #class attribute
    species = "bird"

    #instance attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age
#instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

#access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

#access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))