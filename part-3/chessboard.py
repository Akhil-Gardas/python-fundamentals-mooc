# Write your solution here

# Testing the function
def chessboard(size):
    row = 0
    while row < size:
        line = ""
        col = 0
        while col < size:
            # If the sum of row and col indices is even, print 1, else 0
            if (row + col) % 2 == 0:
                line += "1"
            else:
                line += "0"
            col += 1
        
        print(line)
        row += 1

if __name__ == "__main__":
    chessboard(3)