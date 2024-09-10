print("What is your last name and first name")
First_Name = input("")
last_Name = input("")
S = F'Hi, {last_Name} {First_Name}'
print (S)
str = "First_Name and last_Name"
len(str)  # number of characters in str
print(len(S))
print(f"your initials are {First_Name[0]}{last_Name[0]}")

print("put your name")
input_string = input()
output=""
for i in input_string:
    output = output + i*2
print(output)