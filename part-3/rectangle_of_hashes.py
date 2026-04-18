# Write your solution here
width = int(input("Width: "))
height = int(input("Height: "))

# The loop runs 'height' times
while height > 0:
    # Print a string of hashes multiplied by the width
    print("#" * width)
    # Decrease height by 1 to eventually end the loop
    height -= 1