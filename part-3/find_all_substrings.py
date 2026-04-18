# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")

while True:
    index = word.find(char)
    
    # If character isn't found, stop
    if index == -1:
        break
    
    # Negative check: Is the found index within the first (length - 2) characters?
    # This ensures there's room for a 3-character slice.
    if index <= len(word) - 3:
        print(word[index : index + 3])
    
    # Move past the current character
    word = word[index + 1 :]