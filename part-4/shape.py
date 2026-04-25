# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(length:int,text:str):
    if text=="":
        character="*"
    else:
        character=text[0]
    print(character * length)

def shape(length1:int,character1:str,length2:int,character2:str):
    i=1
    while i<=length1:
        line(i,character1)
        i+=1
    j=0    
    while j<length2:
        line(length1,character2)
        j+=1
            
            

if __name__ == "__main__":
    shape(5, "x", 3, "*")
    print()
    shape(2,"o",4,"+")
    print()
    shape(3,".",0,",")