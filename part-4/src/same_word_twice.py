# Write your solution here
words = []

while True:
    word = input("Word: ")
    
    # Check if the word is already in our list
    if word in words:
        break
    
    # If it's a new word, add it to the list
    words.append(word)

print(f"You typed in {len(words)} different words")