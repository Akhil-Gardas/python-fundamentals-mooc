# Write your solution here
limit = int(input("Limit: "))
number = 1
sum_result = 0

while sum_result < limit:
    sum_result += number
    number += 1

print(sum_result)