# Program for capturing client details
# Initial version for input, pickling, and exporting

# Import packages
import pickle

# Dictionaries used
client_dict = {"first_name":"fname","last_name":"lname","birth_day":"bday"}

# Open up pickle file for data placement
pickle_base = open("dict.pickle","wb")

# Place commands for operations
print("Do you want to add a New Entry (E), see Client List (C)")

# Close pickle file
pickle_base.close()
