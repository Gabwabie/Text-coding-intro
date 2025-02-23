# medical_cause = input("did you have a medical cause Y or N: ")
# atten = int(input("enter the attendance of the student: "))

# if medical_cause == 'Y':
#     print("You are allowed")
# else:
#     if atten>=75:
#         print("Allowed")
#     else:
#         print("Not allowed")

# units = int(input("Please enter number of units you consumed: "))
# if(units<50):
#     amount = units*2.60
#     surcharge = 25
# elif(units<=100):
#     amount = 130+((units - 50)*3.25)
#     surcharge = 35
# elif(units<=200):
#     amount = 130+162.50+((units - 100)*5.26)
#     surcharge = 45
# else:
#     amount = 130+162.50+526+((units - 200)*8.45)
#     surcharge = 75

# total = amount + surcharge
# print("\nElectricity Bill = %.2f" %total)

age = int(input("Enter age: "))
height = float(input("Enter height: "))

if age >17:
    print("Qualified")
else:
    if height > 1.9:
        print("Qualified")
    else:
        print("Try again next time")