# Write your solution here
def length_of_longest(my_list:list):
    highest=0
    for strings in my_list:
        if len(strings)>highest:
            highest=len(strings)
    return highest

if __name__=="__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)
