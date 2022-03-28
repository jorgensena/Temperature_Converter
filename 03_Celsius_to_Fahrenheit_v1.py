""" Converting Celsius to Fahrenheit v1
Converting from degrees Celsius to Fahrenheit
Function takes in a value, does the conversion and puts answer into a list
"""

def to_f(from_c):
    fahren = (from_c * 9 / 5) + 32
    return fahren


# MAIN ROUTINE
temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_f(item)
    ans_statement = f"{item} degrees C to {answer} degrees F"
    converted.append(ans_statement)

for deg in converted:
    print(deg)
