# Write your solution here
while True:
    string = input("Please type in a string: ")
    
    # If the string is empty, the loop ends
    if string == "":
        break
        
    # Print the string and then a line of '-' matching its length
    print(string)
    print("-" * len(string))