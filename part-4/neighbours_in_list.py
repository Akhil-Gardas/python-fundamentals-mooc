# Write your solution here
def longest_series_of_neighbours(my_list:list):
    current_streak=1
    longest=1
    for i in range(1,len(my_list)):
        diff=my_list[i]-my_list[i-1]
        if diff==1 or diff==-1:
            current_streak+=1
        else:
            current_streak=1
        if   current_streak>longest:
            longest=current_streak
    return longest

if __name__=="__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
              
        


