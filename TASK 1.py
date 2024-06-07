import tkinter as tk
from tkinter import messagebox

# Function to add item to the listbox
def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter an item")

# Function to delete the selected item from the listbox
def delete_item():
    try:
        selected_item_index = listbox.curselection()[0]
        listbox.delete(selected_item_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item to delete")

# Function to edit the selected item in the listbox
def edit_item():
    try:
        selected_item_index = listbox.curselection()[0]
        item = entry.get()
        if item:
            listbox.delete(selected_item_index)
            listbox.insert(selected_item_index, item)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an item")
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item to edit")

# Function to update the selected item in the listbox
def update_item():
    try:
        selected_item_index = listbox.curselection()[0]
        item = entry.get()
        if item:
            listbox.delete(selected_item_index)
            listbox.insert(selected_item_index, item)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an item")
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item to update")

# Setting up the main application window
app = tk.Tk()
app.title("To-Do List Application")
app.configure(bg='blue')
app.geometry("500x400")

# Heading Label
heading = tk.Label(app, text="To-Do List Application", bg='blue', fg='white', font=('Arial', 16, 'bold'))
heading.pack(pady=10)

# Frame for Entry and Add Button
frame = tk.Frame(app, bg='blue')
frame.pack(pady=10)

# Entry box
entry = tk.Entry(frame, width=35, bg='white')
entry.grid(row=0, column=2, padx=10)

# Add Button
add_button = tk.Button(frame, text="Add Item", command=add_item)
add_button.grid(row=0, column=1, padx=10)

# Listbox to display items
listbox = tk.Listbox(app, width=50, height=10)
listbox.pack(pady=20)

# Frame for Edit, Update, and Delete Buttons
button_frame = tk.Frame(app, bg='blue')
button_frame.pack(pady=10)

# Edit Button
edit_button = tk.Button(button_frame, text="Edit", command=edit_item, bg='light green', fg='black')
edit_button.grid(row=0, column=0, padx=10)

# Update Button
update_button = tk.Button(button_frame, text="Update", command=update_item, bg='yellow')
update_button.grid(row=0, column=1, padx=10)

# Delete Button
delete_button = tk.Button(button_frame, text="Delete", command=delete_item, bg='red', fg='white')
delete_button.grid(row=0, column=2, padx=10)

# Run the application
app.mainloop()