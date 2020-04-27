# GUI for adding client instances into DB.
# Packages
import sqlite3 as sq
import tkinter as tk

# set SQL - 'clientdatabase.db'
try:
    conn = sq.connect("clientdatabase.db")
    cur = conn.cursor()
except:
    print("DB Initialization Failed")

# GUI Points
entry_point = tk.Tk()
tk.Label(entry_point, text="Full Name").grid(row=0)
tk.Label(entry_point, text="Phone Number").grid(row=1)

# Capture Variables
FName = str(tk.Entry(entry_point))
FName.grid(row=0, column=1)
Phone = str(tk.Entry(entry_point))
Phone.grid(row=1, column=1)

# GUI Interactibles
tk.Button(entry_point, text='Quit', command=entry_point.quit).grid(row=3, column=0, sticky=tk.W, pady=4)

entry_point.mainloop()
