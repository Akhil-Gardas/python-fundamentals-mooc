# Write your solution here
while True:
    editor = input("Editor: ")
    user_choice = editor.lower()
    
    if user_choice == "visual studio code":
        print("an excellent choice!")
        break
    elif user_choice == "word" or user_choice == "notepad":
        print("awful")
    else:
        print("not good")
        