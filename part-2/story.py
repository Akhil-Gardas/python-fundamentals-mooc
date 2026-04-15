# Write your solution here
story = ""
last_word = ""

while True:
    word = input("Please type in a word: ")
    
    # Check if the user wants to end or if they repeated the same word
    if word == "end" or word == last_word:
        break
    
    # Add the word and a space to our story string
    story += word + " "
    last_word = word

# Strip the trailing space before printing
print(story.strip())