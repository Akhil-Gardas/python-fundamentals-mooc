# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum_numbers = 0
positives = 0
negatives = 0

while True:
    number = int(input("Number: "))
    
    if number == 0:
        break
    
    count += 1
    sum_numbers += number
    
    if number > 0:
        positives += 1
    else:
        negatives += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum_numbers}")
print(f"The mean of the numbers is {sum_numbers / count}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")