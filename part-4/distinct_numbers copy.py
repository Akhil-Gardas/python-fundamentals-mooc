# Write your solution here

def distinct_numbers(my_list:list):
    result=[]
    for number in my_list:
        if number not in result:
            result.append(number)
    return sorted(result)
        

if __name__=="__main__":
    my_list=[3,2,2,1,3,3,1]
    print(distinct_numbers(my_list))

