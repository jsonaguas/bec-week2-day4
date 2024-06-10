tasks = []
def main():
    while True:
        ans = input('''Welcome to the To-Do List App!

        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit \n''')
        if ans == '1':
            add_task()
        elif ans == '2':
            view_tasks()
        elif ans == '3':
            mark_task_complete()
        elif ans == '4':
            delete_task()
        elif ans == '5':
            print("Thanks for using the To-Do List App. Have a great day!")
            break
        else:
            print("Invalid input. Please try again.")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task {task} has been added to the list.")
    return

    
def view_tasks():
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")
    return

def mark_task_complete():
    print("Select task to mark complete.")
    view_tasks()
    try:
        task_number = int(input("Enter the task number: "))
        if task_number <= len(tasks):
            print(f"X {task_number}, {tasks[task_number-1]}")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    print("Select task to delete.")
    view_tasks()
    try:
        task_number = int(input("Enter the task number: "))
        if task_number <= len(tasks):
            tasks.pop(task_number-1)
            print(f"Task {task_number}, {tasks[task_number-1]} has been deleted.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

main()
