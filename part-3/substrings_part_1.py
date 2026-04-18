# Write your solution here
string = input("Please type in a string: ")

# We start with a length of 1 and increase it 
# until it reaches the full length of the string
length = 1

while length <= len(string):
    # Slice from the very beginning (0) to the current length
    print(string[0:length])
    length += 1