# # And-Or
# a = 10
# b = 12
# c = 9

# if a and b and c:
#     print("All the numbers have boolean value as True")
# else:
#     print("Atleast one number has boolean value as False")

# a = 10
# b = -10
# c = 0

# if a > 0 or b > 0:
#     print("Either of the number is greater than 0")
# else:
#     print("No number is greater than 0")

# if b > 0 or c > 0:
#      print("Either of the number is greater than 0")
# else:
#     print("No number is greater than 0")

# # Not Equal
# a = 10
# b = 12
# c = 12

# print(a != b)
# print(b != c)

# a = "python"
# b = "coding"

# if a != b:
#     print(a, 'and', b, 'are different.')

# a = 5
# a = 5
# if (a == 5) != (b == 5):
#     print('Hello')

# a = int(input("enter a number "))
# if a%2 != 0:
#     print(a, "is not an even number.")

# BMI calculator
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
BMI = weight / (height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are overweight.")
elif BMI <= 34.9:
    print("You are severely overweight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")