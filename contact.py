import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.create_widgets()
        self.connect_db()
        self.refresh_contact_list()

    def connect_db(self):
        # Connect to MySQL database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ak662002",
            database="contact_book"
        )
        self.cursor = self.conn.cursor()

    def create_widgets(self):
        # Create main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Contact Entry Fields
        tk.Label(main_frame, text="Name").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.name_entry = tk.Entry(main_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(main_frame, text="Phone Number").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.phone_entry = tk.Entry(main_frame)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(main_frame, text="Email").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.email_entry = tk.Entry(main_frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(main_frame, text="Address").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.address_entry = tk.Entry(main_frame)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Button(main_frame, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)

        # Dropdown for Search, Update, and Delete
        tk.Label(main_frame, text="Search").grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.search_entry = tk.Entry(main_frame)
        self.search_entry.insert(0,"Name or phone number")
        self.search_entry.bind("<FocusIn>", self.clear_placeholder)
        self.search_entry.bind("<FocusOut>", self.add_placeholder)
        self.search_entry.grid(row=5, column=1, padx=5, pady=5)



        tk.Button(main_frame, text="Search Contact", command=self.search_contact).grid(row=6, column=0, pady=5)
        tk.Button(main_frame, text="Update Contact", command=self.update_contact).grid(row=6, column=1, pady=5)
        tk.Button(main_frame, text="Delete Contact", command=self.delete_contact).grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(main_frame, text="Show All Contacts", command=self.view_contacts).grid(row=8, column=0, columnspan=2, pady=10)

        # Display Area
        self.text_area = tk.Text(main_frame, height=10, width=50)
        self.text_area.grid(row=9, column=0, columnspan=2, pady=10)

        tk.Button(main_frame, text="Exit", bg="red", command=self.exit_application).grid(row=10, column=0, columnspan=2, pady=10)
    def clear_placeholder(self, event):
        if self.search_entry.get() == "Name or phone number":
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg='black')

    def add_placeholder(self, event):
        if not self.search_entry.get():
            self.search_entry.insert(0, "Name or phone number")
            self.search_entry.config(fg='gray')
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            query = "INSERT INTO contacts (name, phone, email, address) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (name, phone, email, address))
            self.conn.commit()
            messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
            self.clear_entries()
            self.refresh_contact_list()
        else:
            messagebox.showwarning("Input Error", "Name and Phone Number are required.")

    def search_contact(self):
        search_text = self.search_entry.get()
        
        if search_text:
            query = "SELECT id, name, phone, email, address FROM contacts WHERE name LIKE %s OR phone LIKE %s"
            self.cursor.execute(query, (f"%{search_text}%", f"%{search_text}%"))
            results = self.cursor.fetchall()
            if results:
                self.display_results(results)
            else:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, "No contact found.")
        else:
            messagebox.showwarning("Input Error", "Please enter a name or phone number to search.")

    def update_contact(self):
        search_text = self.search_entry.get()
        if search_text:
            query = "SELECT id, name, phone, email, address FROM contacts WHERE name LIKE %s OR phone LIKE %s"
            self.cursor.execute(query, (f"%{search_text}%", f"%{search_text}%"))
            result = self.cursor.fetchone()
            if result:
                contact_id = result[0]
                name = self.name_entry.get() or result[1]
                phone = self.phone_entry.get() or result[2]
                email = self.email_entry.get() or result[3]
                address = self.address_entry.get() or result[4]

                query = "UPDATE contacts SET name = %s, phone = %s, email = %s, address = %s WHERE id = %s"
                self.cursor.execute(query, (name, phone, email, address, contact_id))
                self.conn.commit()
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_entries()
                self.refresh_contact_list()
            else:
                messagebox.showwarning("Not Found", "Contact not found.")
        else:
            messagebox.showwarning("Input Error", "Please enter a name or phone number to update.")

    def delete_contact(self):
        search_text = self.search_entry.get()
        if search_text:
            query = "SELECT id FROM contacts WHERE name LIKE %s OR phone LIKE %s"
            self.cursor.execute(query, (f"%{search_text}%", f"%{search_text}%"))
            result = self.cursor.fetchone()
            if result:
                contact_id = result[0]
                query = "DELETE FROM contacts WHERE id = %s"
                self.cursor.execute(query, (contact_id,))
                self.conn.commit()
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.clear_entries()
                self.refresh_contact_list()
            else:
                messagebox.showwarning("Not Found", "Contact not found.")
        else:
            messagebox.showwarning("Input Error", "Please enter a name or phone number to delete.")

    def view_contacts(self):
        query = "SELECT name, phone, email, address FROM contacts"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        self.display_results(results)

    def display_results(self, results):
        self.text_area.delete(1.0, tk.END)
        if results:
            self.text_area.insert(tk.END, "\n".join(f"Name: {row[0]}\nPhone: {row[1]}\nEmail: {row[2]}\nAddress: {row[3]}\n" for row in results))
        else:
            self.text_area.insert(tk.END, "No contacts found.")

    def refresh_contact_list(self):
        pass  # Refresh contact list is no longer needed

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

    def exit_application(self):
        self.conn.close()
        self.root.destroy()

# Create the main window
root = tk.Tk()
app = ContactBook(root)
root.mainloop()