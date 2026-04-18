# Write your solution here
limit = int(input("Limit: "))
number = 1
sum_result = 0
calculation = ""

while sum_result < limit:
    if number == 1:
        sum_result = 1
        calculation = "1"
    else:
        sum_result += number
        calculation += f" + {number}"
    
    # Increment number for the next potential iteration
    number += 1

print(f"The consecutive sum: {calculation} = {sum_result}")