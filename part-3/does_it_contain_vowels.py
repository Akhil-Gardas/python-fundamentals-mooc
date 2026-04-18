# Write your solution here
string = input("Please type in a string: ")

# Define the vowels we are looking for
vowels = "aeo"

# Loop through each vowel to check if it's in the string
for vowel in vowels:
    if vowel in string:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")