# Write your solution here
item=[]
while True:
    print(f"The list is now {item}")
    character=input("a(d)d, (r)emove or e(x)it:")

    if character=="d":
        if len(item)==0:
            item.append(1)
        else:    
          item.append(item[-1]+1)
    elif character=="r":
        item.pop()
    elif character=="x":
        print("Bye!")
        break


    