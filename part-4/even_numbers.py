# Write your solution here
def even_numbers(my_list: list):
    # This is the most efficient 'Pythonic' way to filter a list
    return [x for x in my_list if x % 2 == 0]

if __name__ == "__main__":
    # You must define the variable before using it as an argument
    original_list = [1, 2, 3, 4, 5]
    
    # Store the result of the function in a new variable
    new_list = even_numbers(original_list)
    
    print("original", original_list)
    print("new", new_list)