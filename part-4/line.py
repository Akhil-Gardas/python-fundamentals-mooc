# Write your solution here
# You can test your function by calling it within the following block
def line(length:int,text:str):
    if text=="":
        character="*"
    else :
        character=text[0]
    print(character*length)        
if __name__ == "__main__":
    line(5, "ram")