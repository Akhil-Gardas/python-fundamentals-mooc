# Write your solution here
# You can test your function by calling it within the following block
def mean(my_list: list):
    return sum(my_list) / len(my_list)

# Testing the function:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print("mean value is", result)