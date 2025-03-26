# Value Error

# try:
#     number = int(input("Enter a number: "))
#     print("The number entered is", number)
# except ValueError as ex:
#     print("Exception:", ex)

# Multiple exceptions

# try: 
#     num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
#     result = num1 / num2
#     print("Result is:", result)
# except ZeroDivisionError:
#     print("Division by zero is error!!")
# except SyntaxError:
#     print("Comma is missing. Enter numbers separated by comma like this 1, 2")
# except:
#     print("Wrong input")
# else:
#     print("No exceptions")
# finally:
#     print("This will execute no matter what")

# Bye Bye

valid = False
while not valid:
    try:
        n = int(input("Enter a number: "))
        while n%2==0:
            print("bye")
        valid = True
    except ValueError:
        print("Invalid")