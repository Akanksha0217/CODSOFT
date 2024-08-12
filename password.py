import tkinter as tk
import random
import string

def generate_password(length=8):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def show_password():
    # Generate an 8-character password
    password = generate_password()
    # Update the password_label text with the generated password
    password_label.config(text=password)

def set_length():
    try:
        # Get the desired password length from the input field
        length = int(length_entry.get())
        if length < 1:
            password_label.config(text="Length must be at least 1.")
        else:
            # Generate a password with the specified length
            password = generate_password(length)
            password_label.config(text=password)
    except ValueError:
        password_label.config(text="Invalid input. Enter a number.")

def exit_application():
    root.destroy()

# Set up the main window
root = tk.Tk()
root.title("Akanksha Password Generator")
root.geometry("300x200")  # Adjusted window size

# Create and place the widgets
tk.Label(root, text="Enter password length:").pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password",bg="green", command=set_length)
generate_button.pack(pady=5)  # Reduced padding

passwork=tk.Label(root,text="Your Generated Password is :").pack()

password_label = tk.Label(root, text="", font=("Helvetica", 16))
password_label.pack(pady=5)  # Reduced padding

exit_button = tk.Button(root, text="Exit", bg="red", command=exit_application)
exit_button.pack(pady=5)  # Increased padding only for separation

# Run the GUI main loop
root.mainloop()
