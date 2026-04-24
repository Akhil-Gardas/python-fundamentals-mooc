# Copy here code of line function from previous exercise
def line(length:int,text:str):
    if text=="":
        character="*"
    else:
        character= text[0]
    print(character * length)   


def square(size:int, character:str):
    # You should call function line here with proper parameters
    i=1
    while True:
      line(size, character)
      if i==size:
        break
      i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "*")
    print()
    square(3,"o")