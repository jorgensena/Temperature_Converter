# Includes RegEx to check filename is valid (A-Z a-z 0-9 and underscores)

import re

# Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank / invalid
# Assume valid data for now
has_error = "yes"
error_type = ""
while has_error == "yes":
    filename = input("Enter a filename: ")
    has_error = "no"

    valid_char = "[A-Za-z0-9]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue  # If the letter is valid, goes back and checks the next

        elif letter == " ":  # Otherwise, find problem
            error_type = "(no spaces allowed)"
        else:
            error_type = f"(no {letter}'s allowed)"
        has_error = "yes"

    if filename == "":
        error_type = "can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print(f"Invalid filename - {error_type}")
    else:
        print("You entered a valid filename")
    print()

# add .txt suffix
filename = filename + ".txt"

# Create file to hole data
f = open(filename, "w+")

for item in data:
    f.write(item + "\n")

# close file
f.close()
