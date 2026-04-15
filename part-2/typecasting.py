# Write your solution here
number = float(input("Please type in a number: "))

# Extract the integer part using the int() function
integer_part = int(number)

# Subtract the integer part from the original number to get the decimal part
decimal_part = number - integer_part

print(f"Integer part: {integer_part}")
print(f"Decimal part: {decimal_part}")