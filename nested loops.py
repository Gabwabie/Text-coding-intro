i = 1
while i<=5:
    j=1
    while j <=10:
        print(j,end=" ")
        j=j+1
    i=i+1
    print()

for i in range(1, 5):
    for j in range(1, 11):
        print(j, end=' ')
    print()

string = input("Please enter a word: ")
char = input("Please enter a character: ")
i = 0
count = 0
while(i < len(string)):
    if (string[i] == char):
        count = count + 1
    i = i + 1
print("The total number of times", char, " has occured = ", count)

lower = int(input("Enter a upper range: "))
upper = int(input("Enter a lower range: "))
print("Prime numbers between", lower, "and", upper, "are: ")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)