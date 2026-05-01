# Write your solution here
# You can test your function by calling it within the following block
def range_of_list(my_list: list):
    return max(my_list) - min(my_list)

# Testing the function:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print("The range of the list is", result)