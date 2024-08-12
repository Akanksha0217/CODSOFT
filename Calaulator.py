import tkinter as tk
from tkinter import messagebox

# Function to perform arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Function to handle the calculation based on user input
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)
        else:
            result = "Invalid operation"
        
        if result == "Error! Division by zero.":
            messagebox.showerror("Error", result)
        else:
            result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numeric values.")

def exit_application():
    root.destroy()

# Setting up the main application window
root = tk.Tk()
root.title("Akanksha Calculator")

# Creating widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

operation_var = tk.StringVar(root)
operation_var.set("Addition")  # Default value

tk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=10)
operation_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate,bg="orange")
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

exit_button=tk.Button(root,text="Exit",bg="red",command=exit_application)
exit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
