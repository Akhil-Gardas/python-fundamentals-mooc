# Write your solution here
word = input("Word: ")

# The frame is 30 characters wide. 
# We subtract 2 for the border stars ('*') on each side.
padding = (28 - len(word)) // 2

# If the word length is odd, one side needs an extra space.
# We use '%' to check if the remaining space is odd.
extra = (28 - len(word)) % 2

print("*" * 30)
print("*" + " " * padding + word + " " * (padding + extra) + "*")
print("*" * 30)