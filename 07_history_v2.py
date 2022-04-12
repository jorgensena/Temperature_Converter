""" Get data from user and store it in a list,
then display the most recent three entries nicely
Trial #2 - uses a deque method (no need for reverse ordering """

# Set up empty list
from collections import deque
calculations = deque()

# Get five items of data
for item in range(0, 5):
    get_item = input("Enter an item: ")
    calculations.append(get_item)

# Show that everything made it into the list
print()
print("----- The Full List -----")
print(calculations)

print()

print("----- Most Recent 3 -----")
for item in range(0, 3):
    print(calculations[item])
