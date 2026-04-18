word = input("Please type in a word: ")
char = input("Please type in a character: ")

# Find the first occurrence of the character
index = word.find(char)

# Check if the character was found (-1 means not found)
# Also check if there are at least 3 characters available from that index
if index != -1 and index + 3 <= len(word):
    print(word[index : index + 3])