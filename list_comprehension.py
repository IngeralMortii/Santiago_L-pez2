num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

obj = ["even" if item %2==0 else "odd" for item in range (1,21)]
print(obj)

#assigment 2

numbers = (1,2,3,4,5,6,7,8,9,10)

cubic = [num*1 for num in numbers if num%3==0]
print(cubic)