
count = 1
total = 0

# BUG: The while statement was missing a colon, so I added : at the end.
while count <= 5:
    # BUG: The loop originally stopped at 4 because it used < 5. I changed it to <= 5 so that 5 is included.
    total = total + count
    count = count + 1

# BUG: The total is an integer, so I changed the + operation to use an f-string instead of joining a string and integer.
print(f"Sum of 1 to 5 is: {total}")