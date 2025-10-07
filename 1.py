import time 
tasks = []

while True: 
    time.sleep(1)
    print("-------------------------")
    print("" ,"1. Add Task\n", "2. View Task\n", "3. Remove Task \n", "4. Exit")

    choice = input('Enter your Choice: ')
    time.sleep(1)
    print("\n\n\n\n\n\n")

    if choice == '1':
        # print("-------------------------")
        task_add = input("Enter your Task here: ")
        time.sleep(1)
        print("-------------------------")
        print("Task Added successfully!")
        print("-------------------------")
        print("\n\n\n\n\n\n")
        tasks.append(task_add)
        time.sleep(1)

    elif choice == '2':
        print("-------------------------")
        print("Your Tasks are: ")
        for i in range(len(tasks)): 
            print(f"{i+1}.", tasks[i])
        # print((i+1), *tasks, sep='\n')
        print("-------------------------")
        time.sleep(1)

        
    elif choice == '3':
        print("-------------------------")
        print("Tasks: ")
        for i in range(len(tasks)): 
            print(f"{i+1}.", tasks[i])

        task_no = int(input("Which Task to Delete ? :"))
        tasks.remove(tasks[task_no-1])
        print("-------------------------")
        time.sleep(1)
        print("Task successfully deleted!")
        print("-------------------------")
        time.sleep(1)

    elif choice == '4' or choice == "Exit" or choice == "exit":
        
        break

    else:
        print("\n-------------------------")
        print("Enter a Valid Choice!")
        print("-------------------------")
        time.sleep(1)
        



