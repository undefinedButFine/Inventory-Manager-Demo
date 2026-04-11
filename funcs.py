def itemSearch():
    searchTarget = input('Enter search item: ')

    with open("items.txt", "r") as file:
        for item in file:
            if searchTarget.lower() == item.lower().strip(): #Removes whitespace otherwise won't find
                print(f"\n {item.strip()} has been found.")
                break
        else:
            print("Item was not found!\n")

def itemAdd():
    addTarget = input('Please enter the name of the item you wish to add: ')

    with open("items.txt", "a") as file: #points to end of file
        file.write(f"\n{addTarget}") #New line otherwise appended to end of previous item
        print(f"Added {addTarget} to file\n")
