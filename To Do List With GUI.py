import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List Application")
        self.tasks = []

        # Create UI elements
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.add_task_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.update_task_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=5)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            messagebox.showinfo("Task Added", f'Task "{task}" added to the list.')

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            old_task = self.tasks[selected_index]
            new_task = simpledialog.askstring("Update Task", f"Update task '{old_task}':")
            if new_task:
                self.tasks[selected_index] = new_task
                self.update_task_listbox()
                messagebox.showinfo("Task Updated", f'Task "{old_task}" updated to "{new_task}".')
        except IndexError:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            removed_task = self.tasks.pop(selected_index)
            self.update_task_listbox()
            messagebox.showinfo("Task Deleted", f'Task "{removed_task}" removed from the list.')
        except IndexError:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Add tasks to the listbox

def main():
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()