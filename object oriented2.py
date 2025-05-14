#Create Class
class IOString():
    #constructor to set default value
    def __init__(self):
        self.str1 = ""

    #function to get input from user
    def get_String(self):
        self.str1 = input("Enter String : ")

    #function to print the string in upper case
    def print_String(self):
        print("Result is :", self.str1.upper())

#object creation
str1 = IOString()

#call functions
str1.get_String()
str1.print_String

#Create Class
class Employee:

    #Initializing
    def __init__(self):
        print('Employee created')
    
    #Calling destructor
    def __del__(self):
        print("Destructor called")

def Create_obj():
    print('Making object...')
    obj = Employee()
    print('function end')
    return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program end...')