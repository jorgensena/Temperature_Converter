# Includes RegEx to check filename is valid (A-Z a-z 0-9 and underscores)

import re

# Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank / invalid
# Assume valid data for now
filename = input("Enter a filename (leave off the extension): ")

valid_file = "[A-Zaz]"
if re.match(valid_file, filename):
    # add .txt suffix
    filename = filename + ".txt"
    # Create file to hole data
    f = open(filename, "w+")

    for item in data:
        f.write(item + "\n")

    # close file
    f.close()

else:
    print("Oops!")
