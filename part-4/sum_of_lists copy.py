# Write your solution here
def list_sum(list1: list, list2: list):
    # zip(list1, list2) pairs them up: (1, 7), (2, 8), (3, 9)
    # Then we just add the two numbers in each pair
    return [a + b for a, b in zip(list1, list2)]

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # Output: [8, 10, 12]