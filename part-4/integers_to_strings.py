# Write your solution here
def formatted(my_list: list):
    new_list = []
    
    for number in my_list:
        # Use an f-string to format to 2 decimal places
        # The :.2f tells Python: "Float with 2 decimal points"
        formatted_string = f"{number:.2f}"
        new_list.append(formatted_string)
        
    return new_list

# Testing the function
if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)