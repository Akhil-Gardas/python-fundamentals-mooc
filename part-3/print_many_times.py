# Write your solution here

# You can test your function by calling it within the following block
def print_many_times(text,times):
    iteration=0
    while iteration<times:
        print(text)
        iteration+=1
if __name__=="__main__":
    print_many_times("hi",5)
    print()
    print_many_times("All Pythons, except one, grow up.",3)