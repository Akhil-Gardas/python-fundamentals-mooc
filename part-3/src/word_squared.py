# Write your solution here
def squared(text, size):
    row = 0
    # This keeps track of which character in the string we are at
    index = 0
    
    while row < size:
        line = ""
        col = 0
        while col < size:
            # Add the character at the current index to our line
            line += text[index]
            
            # Move to the next character, but wrap back to 0 if we hit the end
            index += 1
            if index == len(text):
                index = 0
                
            col += 1
        
        print(line)
        row += 1

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)