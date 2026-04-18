# Write your solution here
# You can test your function by calling it within the following block

def hash_square(length):
    rows = 0
    while rows < length:
        # This prints a line of '#' repeated 'length' times
        print("#" * length)
        rows += 1

# This block is for testing your function
if __name__ == "__main__":
    hash_square(5)