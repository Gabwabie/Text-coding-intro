# Finding average:
num1 = 67
num2 = 100
num3 = 21
num4 = 32
num5 = 15

sum = num1+num2+num3+num4+num5
print("The sum of the 5 numbers is ", sum)

average = sum/5
print("The average of the 5 numbers is ", average)

# Taking total amount as input from user:
Amount =(int(input("Please enter amount for withdraw:")))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print( "notes of 100 TT dollars ", note_1)
print( "notes of 50 TT dollars ", note_2)
print( "notes of 10 TT dollars ", note_3)

# Taking marks as input from user:
print("Enter marks received in the 4 subjects listed below:")
math = int(input("maths: "))
english = int(input("english: "))
science = int(input("science: "))
arabic = int(input("arabic: "))

sum = math+english+science+arabic
print("The sum of marks in the 4 subjects is ", sum)

perc = (sum/400)*100

print("You total percentage is: ")
print(perc)