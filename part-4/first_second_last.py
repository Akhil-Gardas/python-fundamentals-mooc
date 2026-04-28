# Write your solution here
# You can test your function by calling it within the following block
def first_word(sentence: str) -> str:
    words = sentence.split(" ")
    return words[0]

def second_word(sentence: str) -> str:
    words = sentence.split(" ")
    return words[1]

def last_word(sentence: str) -> str:
    words = sentence.split(" ")
    # -1 is the Pythonic way to get the last item in a list
    return words[-1]

if __name__ == "__main__":
    sentence = "it was a dark and stormy python"
    print(first_word(sentence))   # it
    print(second_word(sentence))  # was
    print(last_word(sentence))    # python