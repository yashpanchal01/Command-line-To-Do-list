import time 
tasks = []


def add_task():
    # print("-------------------------")
        task_add = input("Enter your Task here: ")
        time.sleep(1)
        print("-------------------------")
        print("Task Added successfully!")
        print("-------------------------")
        time.sleep(1)
        print("\n\n\n\n\n\n")
        tasks.append(task_add)


def view_task():
        print("\n\n\n\n\n\n")
        time.sleep(1)
        print("-------------------------")
        print("Your Tasks are: ")
        time.sleep(1)
        for i in range(len(tasks)): 
            print(f"{i+1}.", tasks[i])
        # print((i+1), *tasks, sep='\n')
        print("-------------------------")
        time.sleep(2)

def remove_task():
        print("\n\n\n\n\n\n")
        print("-------------------------")
        print("Tasks: ")
        time.sleep(1)
        for i in range(len(tasks)): 
            print(f"{i+1}.", tasks[i])
        time.sleep(1)

        while True:

            task_no = input("Which Task to Delete ? :")

            if task_no.isdigit() and len(task_no) == 1:
                print(f"wait!")
                break
            else:
                print(f"Error: '{task_no}' is not a valid choice!")

        task_no = int(task_no)
        tasks.remove(tasks[task_no-1])
        print("-------------------------")
        time.sleep(1)
        print("Task successfully deleted!")
        print("-------------------------")
        time.sleep(1)
        print("\n\n\n\n\n\n")

def invalid_input():
        print("\n-------------------------")
        print("Enter a Valid Choice!")
        print("-------------------------")
        time.sleep(1)



while True: 
    # time.sleep(1)
    print("-------------------------")
    print("" ,"1. Add Task\n", "2. View Task\n", "3. Remove Task \n", "4. Exit")

    choice = input('Enter your Choice: ')
    # time.sleep(1)
    
    if choice == '1':
         add_task()
    elif choice == '2':
         view_task()  
        
    elif choice == '3':
         remove_task()
        

    elif choice == '4' or choice == "Exit" or choice == "exit":
        break

    else:
         invalid_input()
        
        



