# Initial list of students
#TODO: Create a List of Students names. Add 10 names. Name this list as 'student'
students_names =["Emily Johnson",
"Aiden Smith",
"Sophia Martinez",
"Noah Brown",
"Mia Patel",
"Lucas Kim",
"Ava Garcia",
"Ethan Lee",
"Isabella Davis",
"Liam Wilson"]

def display_students():
    print(f"Current students:\n")
    #TODO HINT: Print each student in the 'students' list
    for element in students_names:
        print(element)
    print(f"___________________________") 

# Add a new student to the list
def add_student():
    
    #TODO HINT: Ask the user for the student's name.
    new_name = input("Enter a new name")
    #TODO Append the student's name to the 'students' list
    students_names.append(new_name)
    #TODO display the updated list
    display_students()

# Remove a student from the list by name
def remove_student():
    #TODO HINT: Ask the user for the student's name to remove
    remove_name = input("Remove a name")
    #TODO Check if the student is in the list, then remove it
    if remove_name in students_names:
        students_names.remove(remove_name)
        display_students()
    #TODO If the student is not found, print an error message
    else:
        print("Invalid name")
    #TODO display the updated list

# remove a student from the end of the list
def pop_student():
    #TODO HINT: Remove the last student from the list
    
    #TODO If the list is not empty, display the name of the student removed
    #TODO If the list is empty, print a message saying there are no students left
    #TODO display the updated list
    pass #! After complete the function remove 'pass'

# Update a student's name in the list
def update_student():
    #TODO HINT: ask for the current name of the student
    #TODO Check if the student is in the list, then ask for the new name
    #TODO Update the student's name in the list
    #TODO If the student is not found, print an error message
    #TODO display the updated list
    pass #! After complete the function remove 'pass'

# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        #TODO depending of the user choice option (1 - 5), call the correct function

# Start the program
