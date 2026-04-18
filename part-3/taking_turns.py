# Write your solution here
number = int(input("Please type in a number: "))

left = 1
right = number

while left <= right:
    print(left)
    left += 1
    
    # Crucial check: make sure we didn't just pass the right pointer
    if left <= right:
        print(right)
        right -= 1