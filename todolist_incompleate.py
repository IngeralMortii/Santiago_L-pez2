# A simple to-do list manager for high school students using functions and list comprehension

# Initial to-do list
todo_list = ["Math homework", "Science project", "Read history book", "Practice piano"]

# Function to display the current to-do list
def display_todo_list():
    print ( f"to do:\n")
    for elements in todo_list:
        print(elements)
    #TODO display the list

# Function to add a new task
def add_task():
    new_task = input("add a new task")
    todo_list.append(new_task)
    display_todo_list()
    #TODO the user wants to add a task. 

# Function to remove a task by its name
def remove_task():
    delete_task = input("delete a task")
    if delete_task in todo_list:
        todo_list.remove(delete_task)
        display_todo_list()
    else:
        print("not valid task")
    #TODO 
    
# Function to find the index of a task
def find_task():
    position = input("what task do you want to know?:")
    if position in todo_list:
        print("your task is number:")
        print(todo_list.index(position))
    
    #The user wants to know in what position is a task. 

# Function to complete and remove the first task
def complete_task():
    comp = input("you want to deleitable the first taks?")
    if comp == "yes" : 
        print(f"you delate:{todo_list.pop(0)}")
        display_todo_list()
    elif comp== "no" :
        print("ok")
        display_todo_list()
    
    #The user wants to remove the first task. 

# Function to filter tasks containing a specific keyword using list comprehension
def filter_tasks():
    keyword = input( "what you want to look for?:")
    task = [task for task in todo_list if keyword in task]
    print(task)
    
    
    #TODO create a list comprehension variable to filter tasks containing a specific keyword
   # filtered_tasks = []
    #print(f"\nTasks containing '{keyword}':")
    #print(filtered_tasks if filtered_tasks else "No tasks found.")

# Main program

# Main menu to choose options
def main():


    while True:
        print("\nTo-Do List Manager Menu")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Find Task")
        print("5. Complete First Task")
        print("6. Filter Tasks by Keyword")
        print("7. Exit")
        
        choice = input("Enter your number:")
        if choice == "1":
            display_todo_list()
        elif choice =="2":
            add_task()
        elif choice =="3":
            remove_task()
        elif choice =="4":
            find_task()
        elif choice =="5":
            complete_task()
        elif choice =="6":
            filter_tasks()
        elif choice =="7":
            break
        
     #   choice = input("\nEnter your choice (1-7): ")

        #TODO create the if staments for the user. 
        

# Run the main function

main()