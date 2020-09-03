def get_task():
   task = input("Select an option 1, 2, 3, 4, 5 or (Q)uit: ") 
   return task

def get_description():
    task = input("Enter task description to search for: ")
    return task

def get_duration():
    task = int(input("Enter task duration: "))
    return task