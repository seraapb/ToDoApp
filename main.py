
tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added succesfully.")
    
def view_tasks():
    if len(tasks) == 0:
        print("no tasks.")
    else:
        print("List of tasks: ")
        for i, task in enumerate(tasks):
            print(f"{i+1}.{task}")
            
def delete_task():
    if len(tasks) == 0:
        print("no tasks to delete")
        
    else:
        print("Tasks: ")
        for i, task in enumerate(tasks):
            print(f"{i+1}.{task}")
            choice = int(input)("Enter the task number to delete: ")
            
            if 0 < choice <= len(tasks):
                del tasks[choice-1]
                print("Task deleted succesfully.")
            else:
                print("Invalid task number.")
        
    






def main():
    while True:
        print("\n -------------- ToDo App -------------- ")
        print("1. Add Task")
        print("2. View Task")
        print("3. Delete Task")
        print("4. Quit ")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task() #Diese Funktion wurde nicht erstellt
            
        elif choice == 2:
            view_task() # """"
            
        elif choice == 3:
            delete_task() #""""""
            
        elif choice == 4:
            print("Thank you for using ToDo App.")
            break
        else:
            print("Invalid choice. Please try again!")
            
main()