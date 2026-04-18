# Write your solution here
string = input("Please type in a string: ")

# We start with an index that points to the last character
# and move backwards toward the beginning (index 0)
n = len(string) - 1

while n >= 0:
    # Slice from the current index 'n' to the end of the string
    print(string[n:])
    n -= 1