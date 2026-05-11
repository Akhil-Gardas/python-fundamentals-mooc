# Write your solution here
def no_vowels(word:str):
    new_string=""
    for char in word:
        if char not in "aeiou":
            new_string=new_string+char
    return(new_string)

if __name__=="__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))

