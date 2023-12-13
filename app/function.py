# Jefferson Collins
# 12/13/23
# function.py

# import SQLlite3 and more
import sqlite3
import tkinter as tk
from tkinter import Label, Entry, Button

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< add Biker functions>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Function to add a new biker to the database
def add_new_biker(first_name, last_name, bike_name, location, years_exp):
    try:
        # Connect to the database
        connection = sqlite3.connect("C:/Users/roger/OneDrive/Documents/Python class/mountain_biking.db")
        cursor = connection.cursor()

        # Insert a new biker into the Biker table
        cursor.execute("""
            INSERT INTO Biker (first_name, last_name, bike_name, location, years_exp)
            VALUES (?, ?, ?, ?, ?)
        """, (first_name, last_name, bike_name, location, years_exp))

        # Commit changes and close the connection
        connection.commit()
        connection.close()

        print("Biker added successfully.")

    except Exception as e:
        print(f"Error adding biker: {e}")

# Function to handle the "Add biker" button click
def add_biker_window():
    add_window = tk.Toplevel()
    add_window.title("Add Biker")

    # Labels and Entry widgets for user input
    first_name_label = Label(add_window, text="First Name:")
    first_name_entry = Entry(add_window)

    last_name_label = Label(add_window, text="Last Name:")
    last_name_entry = Entry(add_window)

    bike_name_label = Label(add_window, text="Bike Name:")
    bike_name_entry = Entry(add_window)

    location_label = Label(add_window, text="Location:")
    location_entry = Entry(add_window)

    years_exp_label = Label(add_window, text="Years of Experience:")
    years_exp_entry = Entry(add_window)

    # Function to handle adding a new biker when the "Submit" button is clicked
    def submit_biker():
        # Get values from Entry widgets
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        bike_name = bike_name_entry.get()
        location = location_entry.get()
        years_exp = years_exp_entry.get()

        # Call the add_new_biker function with user input
        add_new_biker(first_name, last_name, bike_name, location, years_exp)

        # Close the add_window after submitting
        add_window.destroy()

    # Button to submit the new biker
    submit_button = Button(add_window, text="Submit", command=submit_biker)

    # Layout the widgets
    first_name_label.grid(row=0, column=0)
    first_name_entry.grid(row=0, column=1)

    last_name_label.grid(row=1, column=0)
    last_name_entry.grid(row=1, column=1)

    bike_name_label.grid(row=2, column=0)
    bike_name_entry.grid(row=2, column=1)

    location_label.grid(row=3, column=0)
    location_entry.grid(row=3, column=1)

    years_exp_label.grid(row=4, column=0)
    years_exp_entry.grid(row=4, column=1)

    submit_button.grid(row=5, column=1)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< list all the bikers functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function to get a list of all bikers from the database
def get_all_bikers():
    try:
        # Connect to the database
        connection = sqlite3.connect("C:/Users/roger/OneDrive/Documents/Python class/mountain_biking.db")
        cursor = connection.cursor()

        # Fetch all bikers from the Biker table
        cursor.execute("SELECT * FROM Biker")
        bikers = cursor.fetchall()

        # Close the connection
        connection.close()

        return bikers

    except Exception as e:
        print(f"Error fetching bikers: {e}")
        return []

# Function to update the Listbox with the list of bikers
def list_bikers(bikers_listbox):
    bikers_listbox.delete(0, tk.END)  # Clear existing entries

    # Get the list of bikers
    bikers = get_all_bikers()

    # Display bikers in the Listbox
    for biker in bikers:
        bikers_listbox.insert(tk.END, f"{biker[0]} - {biker[1]} {biker[2]} ({biker[5]} years of experience)")


# <<<<<<<<<<<<<<<<<<<<<<<<<<< update bikers functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function to update a biker in the database
def update_biker_in_database(biker_id, first_name, last_name, bike_name, location, years_exp):
    try:
        # Connect to the database
        connection = sqlite3.connect("C:/Users/roger/OneDrive/Documents/Python class/mountain_biking.db")
        cursor = connection.cursor()

        # Update the biker in the Biker table
        cursor.execute("""
            UPDATE Biker
            SET first_name=?, last_name=?, bike_name=?, location=?, years_exp=?
            WHERE biker_id=?
        """, (first_name, last_name, bike_name, location, years_exp, biker_id))

        # Commit changes and close the connection
        connection.commit()
        connection.close()

        print("Biker updated in the database.")

    except Exception as e:
        print(f"Error updating biker in the database: {e}")

# Function to open the update biker window
def open_update_biker_window(root, listbox):
    update_window = tk.Toplevel(root)
    update_window.title("Update Biker")

    biker_label = tk.Label(update_window, text="Select a biker to update:")
    biker_listbox = tk.Listbox(update_window)

    connection = sqlite3.connect("C:/Users/roger/OneDrive/Documents/Python class/mountain_biking.db")
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT biker_id, first_name, last_name FROM Biker")
        bikers = cursor.fetchall()
        for biker in bikers:
            biker_listbox.insert(tk.END, f"{biker[0]} - {biker[1]} {biker[2]}")
    except sqlite3.Error as e:
        print("Error fetching biker names from the database:", e)
    finally:
        connection.close()

    first_name_label = tk.Label(update_window, text="First Name:")
    first_name_entry = tk.Entry(update_window)

    last_name_label = tk.Label(update_window, text="Last Name:")
    last_name_entry = tk.Entry(update_window)

    bike_name_label = tk.Label(update_window, text="Bike Name:")
    bike_name_entry = tk.Entry(update_window)

    location_label = tk.Label(update_window, text="Location:")
    location_entry = tk.Entry(update_window)

    years_exp_label = tk.Label(update_window, text="Years of Experience:")
    years_exp_entry = tk.Entry(update_window)

    def load_biker_details():
        selected_biker = biker_listbox.get(tk.ACTIVE).split(" - ")[0]

        connection = sqlite3.connect("C:/Users/roger/OneDrive/Documents/Python class/mountain_biking.db")
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT * FROM Biker WHERE biker_id=?", (selected_biker,))
            biker_details = cursor.fetchone()

            first_name_entry.insert(tk.END, biker_details[1])
            last_name_entry.insert(tk.END, biker_details[2])
            bike_name_entry.insert(tk.END, biker_details[3])
            location_entry.insert(tk.END, biker_details[4])
            years_exp_entry.insert(tk.END, biker_details[5])

        except sqlite3.Error as e:
            print("Error fetching biker details from the database:", e)
        finally:
            connection.close()

    load_button = tk.Button(update_window, text="Load Biker Details", command=load_biker_details)

    # load changes into database that were made in the update popup window
    def update_biker_in_database_command():
        selected_biker = biker_listbox.get(tk.ACTIVE).split(" - ")[0]
        update_biker_in_database(
            selected_biker,
            first_name_entry.get(),
            last_name_entry.get(),
            bike_name_entry.get(),
            location_entry.get(),
            years_exp_entry.get()
        )

    update_button = tk.Button(update_window, text="Update Biker", command=update_biker_in_database_command)

    biker_label.pack()
    biker_listbox.pack(pady=10)
    load_button.pack()

    first_name_label.pack()
    first_name_entry.pack()

    last_name_label.pack()
    last_name_entry.pack()

    bike_name_label.pack()
    bike_name_entry.pack()

    location_label.pack()
    location_entry.pack()

    years_exp_label.pack()
    years_exp_entry.pack()

    update_button.pack()


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< delete bikers functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function to delete a biker from the database
def delete_biker_from_database(biker_id):
    try:
        # Connect to the database
        connection = sqlite3.connect("C:/Users/roger/OneDrive/Documents/Python class/mountain_biking.db")
        cursor = connection.cursor()

        # Delete the biker from the Biker table
        cursor.execute("DELETE FROM Biker WHERE biker_id=?", (biker_id,))

        # Commit changes and close the connection
        connection.commit()
        connection.close()

        print("Biker deleted from the database.")

    except Exception as e:
        print(f"Error deleting biker from the database: {e}")

# Function to open the delete biker window
def open_delete_biker_window(root, listbox):
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Biker")

    biker_label = tk.Label(delete_window, text="Select a biker to delete:")
    biker_listbox = tk.Listbox(delete_window)

    connection = sqlite3.connect("C:/Users/roger/OneDrive/Documents/Python class/mountain_biking.db")
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT biker_id, first_name, last_name FROM Biker")
        bikers = cursor.fetchall()
        for biker in bikers:
            biker_listbox.insert(tk.END, f"{biker[0]} - {biker[1]} {biker[2]}")
    except sqlite3.Error as e:
        print("Error fetching biker names from the database:", e)
    finally:
        connection.close()

    # function to connect to button in the main.py
    def delete_biker_from_database_command():
        selected_biker = biker_listbox.get(tk.ACTIVE).split(" - ")[0]
        delete_biker_from_database(selected_biker)

        # Refresh the list after deletion
        list_bikers(listbox)

    delete_button = tk.Button(delete_window, text="Delete Biker", command=delete_biker_from_database_command)

    biker_label.pack()
    biker_listbox.pack(pady=10)
    delete_button.pack()

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<< end of code <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

