Menu = input("(H)ello\n(G)oodbye\n(Q)uit\n")
name = input("Enter name: ")
choice = Menu
while choice != "Q":
    if choice == "H":
        print("Hello,", name)
    elif choice == "G":
        print("Goodbye ", name)
    else:
        print("Invalid number")
    name = input("Enter name: ")
    choice = Menu
print("Finished")
