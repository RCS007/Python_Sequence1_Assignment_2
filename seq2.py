# Problem 2:
# Write a Python program that prompts the user for two integer values and displays the
# result of the first number divided by the second, with exactly two decimal places displayed.

# Input two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Perform division and format the result to 2 decimal places
result = num1 / num2

# Display the result
print(f"The result is: {result:.2f}")
