# Jefferson Collins
# 12/13/23
# main.py

# import functions and tkinter
from app.function import add_biker_window, list_bikers, open_update_biker_window, open_delete_biker_window
import tkinter as tk

# main function to call up GUI and other functions
def main():
    # Create the main GUI window
    root = tk.Tk()
    root.geometry("800x600")  # Set the size of the window

    # Listbox to display bikers
    bikers_listbox = tk.Listbox(root, width=80)  # Set the width to fit the window
    bikers_listbox.pack(fill=tk.X)  # Make the Listbox fill the width

    # Button to trigger the "Add Biker" window
    add_biker_button = tk.Button(root, text="Add Biker", command=add_biker_window)
    add_biker_button.pack()

    # Button to list bikers in the Listbox
    list_bikers_button = tk.Button(root, text="List Bikers", command=lambda: list_bikers(bikers_listbox))
    list_bikers_button.pack()

    # Button to trigger the "Update Biker" window
    update_biker_button = tk.Button(root, text="Update Biker", command=lambda: open_update_biker_window(root, bikers_listbox))
    update_biker_button.pack()

    # Button to trigger the "Delete Biker" window
    delete_biker_button = tk.Button(root, text="Delete Biker", command=lambda: open_delete_biker_window(root, bikers_listbox))
    delete_biker_button.pack()

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
