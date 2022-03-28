""" Converting Fahrenheit to Celsius v1
Converting from degrees Fahrenheit to Celsius
Function takes in a value, does the conversion and puts answer into a list
"""

def to_c(from_f):
    celsius = (from_f - 32) * 5 / 9
    return celsius


# MAIN ROUTINE
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = f"{item} degrees F to {answer} degrees C"
    converted.append(ans_statement)

for deg in converted:
    print(deg)
