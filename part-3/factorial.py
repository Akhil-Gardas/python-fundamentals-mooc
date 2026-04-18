while True:
    limit = int(input("Please type in a number: "))
    
    # If the user types 0 or less, we exit the loop immediately
    if limit <= 0:
        print("Thanks and bye!")
        break 
    
    # If the number is positive, we calculate the factorial
    result = 1
    i = 1
    while i <= limit:
        result *= i
        i += 1
        
    print(f"The factorial of the number {limit} is {result}")