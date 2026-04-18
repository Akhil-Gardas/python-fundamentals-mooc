# Write your solution here
string = input("Please type in a string: ")

# Calculate how many stars are needed
stars_needed = 20 - len(string)

# Print the stars followed by the string
print("*" * stars_needed + string)