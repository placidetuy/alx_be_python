# pattern_drawing.py

# Step 1: Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Step 2: Initialize the row counter
row = 0

# Step 3: Draw the pattern using a while loop
while row < size:
    for _ in range(size):  # Print asterisks in a row
        print("*", end="")
    print()  # Move to the next line after printing one row
    row += 1  # Increment the row counter

