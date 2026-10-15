# Python program for addition and subtraction

# Step 1: Take two numbers as input from the user
# float() allows the program to handle both whole numbers and decimals
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform the arithmetic operations
total_sum = num1 + num2
difference = num1 - num2

# Step 3: Print the results
print(f"\nResults:")
print(f"Addition: {num1} + {num2} = {total_sum}")
print(f"Subtraction: {num1} - {num2} = {difference}")
