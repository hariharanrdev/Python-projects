import tkinter as tk
from task import Task

class TaskManagementTool:
    def __init__(self, root):
        self.root = root
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        # Create frames and labels
        self.frame_tasks = tk.Frame(self.root)
        self.frame_tasks.pack(fill="both", expand=True)

        self.label_tasks = tk.Label(self.frame_tasks, text="Tasks:")
        self.label_tasks.pack()

        # Create task list box
        self.listbox_tasks = tk.Listbox(self.frame_tasks, width=40)
        self.listbox_tasks.pack(fill="both", expand=True)

        # Create buttons
        self.button_add_task = tk.Button(self.frame_tasks, text="Add Task", command=self.add_task)
        self.button_add_task.pack()

        self.button_update_task = tk.Button(self.frame_tasks, text="Update Task", command=self.update_task)
        self.button_update_task.pack()

        self.button_delete_task = tk.Button(self.frame_tasks, text="Delete Task", command=self.delete_task)
        self.button_delete_task.pack()

        self.button_exit = tk.Button(self.frame_tasks, text="Exit", command=self.root.destroy)
        self.button_exit.pack()

        self.button_priority = tk.Button(self.frame_tasks, text="Set Priority", command=self.set_priority)
        self.button_priority.pack()

    def add_task(self):
        # Create a new task window
        self.window_add_task = tk.Toplevel(self.root)
        self.window_add_task.title("Add Task")

        # Create labels and entry fields
        self.label_title = tk.Label(self.window_add_task, text="Title:")
        self.label_title.pack()
        self.entry_title = tk.Entry(self.window_add_task, width=40)
        self.entry_title.pack()

        self.label_deadline = tk.Label(self.window_add_task, text="Deadline:")
        self.label_deadline.pack()
        self.entry_deadline = tk.Entry(self.window_add_task, width=40)
        self.entry_deadline.pack()

        # Create add task button
        self.button_add = tk.Button(self.window_add_task, text="Add Task", command=self.add_task_to_list)
        self.button_add.pack()

    def add_task_to_list(self):
        # Get the task details from the entry fields
        title = self.entry_title.get()
        deadline = self.entry_deadline.get()

        # Create a new task object
        task = Task(title, deadline, "Low")

        # Add the task to the list
        self.tasks.append(task)
        self.listbox_tasks.insert(tk.END, str(task))

        # Close the add task window
        self.window_add_task.destroy()

    def update_task(self):
        # Create a new update task window
        self.window_update_task = tk.Toplevel(self.root)
        self.window_update_task.title("Update Task")

        # Create labels and entry fields
        self.label_title_update = tk.Label(self.window_update_task, text="Title:")
        self.label_title_update.pack()
        self.entry_title_update = tk.Entry(self.window_update_task, width=40)
        self.entry_title_update.pack()

        self.label_deadline_update = tk.Label(self.window_update_task, text="Deadline:")
        self.label_deadline_update.pack()
        self.entry_deadline_update = tk.Entry(self.window_update_task, width=40)
        self.entry_deadline_update.pack()

        # Create update task button
        self.button_update = tk.Button(self.window_update_task, text="Update Task", command=self.update_task_in_list)
        self.button_update.pack()

    def update_task_in_list(self):
        # Get the task details from the entry fields
        title = self.entry_title_update.get()
        deadline = self.entry_deadline_update.get()

        # Find the task in the list and update it
        for i, task in enumerate(self.tasks):
            if task.title == title:
                task.deadline = deadline
                self.tasks[i] = task
                self.listbox_tasks.delete(0, tk.END)
                for task in self.tasks:
                    self.listbox_tasks.insert(tk.END, str(task))
                break

        # Close the update task window
        self.window_update_task.destroy()

    def delete_task(self):
        # Get the selected task
        selected_index = self.listbox_tasks.curselection()
        if selected_index:
            selected_task = self.tasks[selected_index[0]]
            self.tasks.remove(selected_task)
            self.listbox_tasks.delete(selected_index)

    def set_priority(self):
        # Create a new set priority window
        self.window_set_priority = tk.Toplevel(self.root)
        self.window_set_priority.title("Set Priority")

        # Create labels and entry fields
        self.label_title_priority = tk.Label(self.window_set_priority, text="Title:")
        self.label_title_priority.pack()
        self.entry_title_priority = tk.Entry(self.window_set_priority, width=40)
        self.entry_title_priority.pack()

        self.label_priority = tk.Label(self.window_set_priority, text="Priority:")
        self.label_priority.pack()
        self.entry_priority = tk.Entry(self.window_set_priority, width=40)
        self.entry_priority.pack()

        # Create set priority button
        self.button_set_priority = tk.Button(self.window_set_priority, text="Set Priority", command=self.set_priority_in_list)
        self.button_set_priority.pack()

    def set_priority_in_list(self):
        # Get the task details from the entry fields
        title = self.entry_title_priority.get()
        priority = self.entry_priority.get()

        # Find the task in the list and update its priority
        for i, task in enumerate(self.tasks):
            if task.title == title:
                task.priority = priority
                self.tasks[i] = task
                self.listbox_tasks.delete(0, tk.END)
                for task in self.tasks:
                    self.listbox_tasks.insert(tk.END, str(task))
                break

        # Close the set priority window
        self.window_set_priority.destroy()

# Create the main window
root = tk.Tk()
root.title("Task Management Tool")

# Create an instance of the TaskManagementTool class
tool = TaskManagementTool(root)

# Start the main loop
root.mainloop()