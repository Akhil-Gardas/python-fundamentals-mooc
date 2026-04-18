# Write your solution here
string1=input("Please type in string 1:")
string2=input("Please type in string 2:")
n1=len(string1)
n2=len(string2)
if n1>n2:
    print(f"{string1} is longer ")
elif n2>n1:
    print(f"{string2} is longer ")    
else:
    print("The strings are equally long")    
