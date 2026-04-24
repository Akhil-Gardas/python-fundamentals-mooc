# Copy here code of line function from previous exercise
def line(length:int,text:str):
    if text=="":
        character="*"
    else :
        character=text[0]
    print(character * length) 

def box_of_hashes(size:int):
    i=0
    while i<size:
        line(10,"#")
        i+=1


if __name__== "__main__":
   box_of_hashes(5)