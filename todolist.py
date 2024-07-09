class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Completed task: {self.tasks[index]['task']}")
        else:
            print("Invalid task number")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Removed task: {removed_task['task']}")
        else:
            print("Invalid task number")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for i, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} - {status}")

# Sample usage
if _name_ == "_main_":
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the task number to mark as completed: "))
            todo_list.complete_task(index)
        elif choice == "3":
            index = int(input("Enter the task number to remove: "))
            todo_list.remove_task(index)
        elif choice == "4":
            todo_list.list_tasks()
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
