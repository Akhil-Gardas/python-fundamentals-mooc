# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(word: str):
    # This is the most efficient way: it compares the word 
    # to its own reverse using a "slice"
    return word == word[::-1]

# Main program (Must NOT be in an if __name__ == "__main__" block for this exercise)
while True:
    user_input = input("Please type in a palindrome: ")
    if palindromes(user_input):
        print(f"{user_input} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")