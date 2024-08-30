Num1 = int(input("Enter the first integer: "))
Num2 = int(input("Enter the second integer: "))

if Num1 > Num2:
    Num1, Num2 = Num2, Num1

for number in range(Num1, Num2 + 1):
    if(number - Num1) % 2 ==0:
        print(f"The square of{number} is {number ** 2}")
        
