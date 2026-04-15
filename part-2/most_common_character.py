# Write your solution here
def most_common_character(word):
    most_frequent_character=word[0]
    for current_character in word:
        
        if word.count(current_character)>word.count(most_frequent_character):
            most_frequent_character=current_character
    return most_frequent_character        

            

if __name__=="__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))


