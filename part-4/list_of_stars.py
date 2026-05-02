# Write your solution here
def list_of_stars(my_list:list):
    for item in my_list:
       for i in range(item):
        print("*",end="")
       print()
  

if __name__=="__main__":
   list_of_stars([3,7,1,1,2])