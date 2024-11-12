from task import Task

class TaskManagementTool:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, deadline, priority):
        task = Task(title, deadline, priority)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self, title, new_deadline=None, new_priority=None, new_status=None):
        for task in self.tasks:
            if task.title == title:
                if new_deadline:
                    task.deadline = new_deadline
                if new_priority:
                    task.priority = new_priority
                if new_status:
                    task.status = new_status
                print(f"Task '{title}' updated successfully!")
                return
        print(f"Task '{title}' not found.")

    def run(self):
        while True:
            print("Task Management Tool")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Enter task title: ")
                deadline = input("Enter task deadline: ")
                priority = input("Enter task priority (High/Medium/Low): ")
                self.add_task(title, deadline, priority)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                title = input("Enter task title to update: ")
                new_deadline = input("Enter new deadline (optional): ")
                new_priority = input("Enter new priority (optional): ")
                new_status = input("Enter new status (optional): ")
                self.update_task(title, new_deadline, new_priority, new_status)
            elif choice == "4":
                print("Exiting the application.")
                break
            else:
                print("Invalid option. Please try again.")