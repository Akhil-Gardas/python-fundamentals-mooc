# Write your solution here
def no_shouting(my_list:list):
    pruned_list=[word for word in my_list if not word.isupper()]
    return pruned_list
if __name__=="__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)