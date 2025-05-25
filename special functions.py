class student:
    __sclname = "Codingal"
    classname = "G8"

    def __init__(self,name):
        self.name = name
    
    def acc(self):
        print(self.__sclname)

std = student("Gabby")

print(std.name)
print(std.classname)

std.acc()

class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

#change the price
c.__maxprice = 1000
c.sell()

#using setter function
c.setMaxPrice(1000)
c.sell()

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        #Method to print points in coordinate format
        def __str__(self):
            return "({0}, {1})".format(self.x, self.y)
        
#Create an object
p1 = Point(2,3)
print(p1)