# Packages
import sqlite3 as sq
import tkinter as tk

# set SQL - 'clientdatabase.db'
try:
    conn = sq.connect("clientdatabase.db")
    cur = conn.cursor()
except:
    print("DB Initialization Failed")
# DB Entry
def client_add():
    print(FName.get())
    print(Phone.get())
    final_tag = 0
    return final_tag

# GUI Points
entry_point = tk.Tk()
entry_point.title("Client List App")
tk.Label(entry_point, text="Full Name").grid(row=0)
tk.Label(entry_point, text="Phone Number").grid(row=1)
tk.Label(entry_point, text="E-Mail").grid(row=2)
tk.Label(entry_point, text="Emerg Contact").grid(row=3)
tk.Label(entry_point, text="Emerg Phone").grid(row=4)

# Capture Variables
FName = tk.Entry(entry_point)
FName.grid(row=0, column=1)
Phone = tk.Entry(entry_point)
Phone.grid(row=1, column=1)
email = tk.Entry(entry_point)
email.grid(row=2, column=1)
e_con = tk.Entry(entry_point)
e_con.grid(row=3, column=1)
e_phon = tk.Entry(entry_point)
e_phon.grid(row=4, column=1)

# GUI Interactibles
tk.Button(entry_point, text='Quit', command=entry_point.quit).grid(row=5, column=0, sticky=tk.W, pady=4)
tk.Button(entry_point, text='Submit', command=client_add).grid(row=5, column=1, sticky=tk.W, pady=4)

entry_point.mainloop()
