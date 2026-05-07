# Write your solution here
def all_the_longest(my_list: list):
    # 1. Find the length of the longest string once
    max_len = len(max(my_list, key=len))
    
    # 2. Use list comprehension to filter the list in one line
    return [word for word in my_list if len(word) == max_len]

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']