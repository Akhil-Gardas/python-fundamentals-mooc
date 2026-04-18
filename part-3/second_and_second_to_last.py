# Write your solution here
string=input("Please type in a string:")
n=len(string)-1
if n>=0:
    if string[1]==string[n-1]:
        print(f"The second and the second to last characters are {string[1]}")
    else:
        print("The second and the second to last characters are different")
n-=1            

