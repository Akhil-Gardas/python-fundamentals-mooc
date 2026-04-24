# Copy here code of line function from previous exercise
def line(length:int,text:str):
    if text=="":
        character="*"
    else :
        character=text[0]
    print(character * length) 

def square_of_hashes(size:int):
    i=0
    while i<size:
        line(size,"#")
        i+=1


if __name__== "__main__":
   square_of_hashes(5)
   print()
   square_of_hashes(3)