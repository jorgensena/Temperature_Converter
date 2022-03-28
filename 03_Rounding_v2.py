""" Display output using rounding for floats only
"""

to_round = [1/1, 1/2, 1/3]
print("------ Numbers to Round ------")
print(to_round)

print()
print("------ Rounded Numbers ------")

for num in to_round:
    if num % 1 == 0:
        print(f"{num:.0f}")
    else:
        print(f"{num:.1f}")
