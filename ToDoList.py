tasks = []

def add_task(description):
    tasks.append({"description": description, "completed": False})

def list_tasks():
    for index, task in enumerate(tasks):
        status = "X" if task["completed"] else " "
        print(f"[{index + 1}] [{status}] {task['description']}")

def complete_task(task_index):
    if 0 < task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
            print("Task added.")
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            task_index = int(input("Enter task index to complete: "))
            complete_task(task_index)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()