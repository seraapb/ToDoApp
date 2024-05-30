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