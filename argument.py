#Tip to waiter
def total_calc(bill_amount,tip_perc):
    total = bill_amount*(1+0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")
total_calc(150,20)

#Cube
def cube(number):
    return number*number*number
def by_three(number):
    if number %3 ==0:
       return cube(number)
    else:
        return False
print(by_three(9))
print(by_three(4))

#Factorial
def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("the factorial of 0:",factorial(0))
print("the factorial of 1:",factorial(1))
print("the factorial of 2:",factorial(4))
print("the factorial of 3:",factorial(5))