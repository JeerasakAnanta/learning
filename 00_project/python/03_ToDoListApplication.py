# To-Do List Application

# tasks is a list of dictionaries, each dictionary representing a task
tasks = [
    {"id": 1, "title": "Buy groceries", "done": False},
    {"id": 2, "title": "Clean the house", "done": False},
    {"id": 3, "title": "Do laundry", "done": False},
    {"id": 4, "title": "Study for exam", "done": False},
]

# function to add a task to the list
def add_task(title):
    new_task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(new_task)

# function to mark a task as completed
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            break

# function to delete a task from the list
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break

# function to print the list of tasks
def print_tasks():
    print("To-Do List:")
    for task in tasks:
        print(f"{task['id']}. {task['title']} {'Done' if task['done'] else ''}")

# main function
def main():
    while True:
        print_tasks()
        print("1. Add task")
        print("2. Mark task as completed")
        print("3. Delete task")
        print("4. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Enter the title of the task: ")
            add_task(title)
        elif choice == "2":
            task_id = int(input("Enter the ID of the task to mark as completed: "))
            complete_task(task_id)
        elif choice == "3":
            task_id = int(input("Enter the ID of the task to delete: "))
            delete_task(task_id)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
