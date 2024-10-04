#Homogeneus list
integers = [1, 2, 3, 8, 33]

animals = ["dog", "cat", "goat"]

names = ["Juan", "Felix", "Carlos"]

float = [2.2, 4.5, 9.8, 10.8]

#Heterogeneus List

numbers_animals_names = [2, "cat", 34.33, "Travis"]


list_lists = [[1,2,3], ["cat", "dog", "goat"]]


#How to access an element in a list 

list = [3, 22, 30, 5.3, 20]

print(list[2])

print(list[0])

print(list[1])

print(list[4])


list_of_squares =[]
for int in range (1,10):
    square = int **2
    list_of_squares.append(square)
    
print(list_of_squares)

#[expression for item in list if condition]

#squared2=[item**2 for item in range (1,10)]

#print(squared2)

#numbers = [1,2,3,4,5,6,7,8,9]


#cubic = [number**3 for number in numbers]
#print(cubic)




numbers = [1,2,3,4,5,6,7,8,9]

doubled_numbers = [num*2 for num in numbers if num%2 == 0]

print(doubled_numbers)