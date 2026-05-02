# Write your solution here
def sum_of_positives(my_list: list):
    # This is a generator expression: "sum every x for each x in the list if x > 0"
    return sum(x for x in my_list if x > 0)

if __name__ == "__main__":
    numbers = [1, -2, 3, -4, 5]
    print("The result is", sum_of_positives(numbers))