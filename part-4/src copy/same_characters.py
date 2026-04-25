# Write your solution here
# You can test your function by calling it within the following block
def same_chars(text:str,i:int,j:int):
    
    if i<0 or i>= len(text) or j<0 or j>=len(text):
        return False
    character1=text[i]
    character2=text[j]
    
    if character1==character2:
        return True
    else :
        return False    



if __name__ == "__main__":
    print(same_chars("programmer", 6, 7))
    print(same_chars("programmer", 0, 4))
    print(same_chars("programmer", 0, 12))