import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = self.load_tasks()

        # Create Widgets
        self.task_entry = tk.Entry(root, width=50,)
        self.task_entry.insert(0, "Enter your task")
        self.task_entry.bind("<FocusIn>", self.clear_placeholder)
        self.task_entry.bind("<FocusOut>", self.add_placeholder)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task,bg="pink",font="Contcansns 10 bold")
        self.add_button.pack(pady=5)

        # Create a Treeview for displaying tasks
        self.tree = ttk.Treeview(root, columns=('Task', 'Status'), show='headings')
        self.tree.heading('Task', text='Task')
        self.tree.heading('Status', text='Status')

         # Set custom styles for the Treeview
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=("Contcansns", 10, "bold"), foreground="green")
        self.tree.pack(pady=10)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_as_completed,bg="pink",font="Contcansns 10 bold")
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task,bg="pink",font="Contcansns 10 bold")
        self.delete_button.pack(pady=5)

        self.load_tasks_into_tree()

    def clear_placeholder(self, event):
        if self.task_entry.get() == "Enter your task":
            self.task_entry.delete(0, tk.END)
            self.task_entry.config(fg='black')

    def add_placeholder(self, event):
        if not self.task_entry.get():
            self.task_entry.insert(0, "Enter your task")
            self.task_entry.config(fg='gray')

    def add_task(self):
        task = self.task_entry.get()
        if task and task != "Enter your task":
            self.tasks.append({'task': task, 'completed': False})
            self.save_tasks()
            self.load_tasks_into_tree()
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, "Enter your task")
            messagebox.showinfo("Task Added", f"Task '{task}' added successfully!")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")

    def mark_as_completed(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_id = selected_item[0]
            item = self.tree.item(item_id)
            task_text = item['values'][0]
            for task in self.tasks:
                if task['task'] == task_text:
                    if not task['completed']:
                        task['completed'] = True
                        self.save_tasks()
                        self.load_tasks_into_tree()
                        messagebox.showinfo("Task Updated", "Task marked as completed!")
                    else:
                        messagebox.showinfo("Info", "Task is already completed")
                    break
        else:
            messagebox.showwarning("Warning", "No task selected")

    def delete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_id = selected_item[0]
            item = self.tree.item(item_id)
            task_text = item['values'][0]
            self.tasks = [task for task in self.tasks if task['task'] != task_text]
            self.save_tasks()
            self.load_tasks_into_tree()
            messagebox.showinfo("Task Deleted", f"Task '{task_text}' deleted successfully!")
        else:
            messagebox.showwarning("Warning", "No task selected")

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f)

    def load_tasks_into_tree(self):
        self.tree.delete(*self.tree.get_children())
        for task in self.tasks:
            status = "Completed" if task['completed'] else "Pending"
            self.tree.insert('', tk.END, values=(task['task'], status))

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
