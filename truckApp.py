from truck import Node, Stack, truck

def main():
    tStack = Stack()
    userTruck = truck()
    userFinish = False

    while True:
        if userFinish == True:
            break
        userInit = input("Welcome to Wasin's Logistics Arrangement!\nPress 'y' to start stacking items\nPress 'x' to exit\n")
        if userInit.lower() == "y":
            while True:
                if userFinish == True:
                    break
                print("\nSelect a truck to load, input respective number only")
                for elem in userTruck.options:
                    print(str(elem["ID"]) + ")",elem["Size"],elem["Type"])
                userSelectedTruck = input()
                try :    
                    userSelectedTruck = int(userSelectedTruck)
                    if userSelectedTruck <= 0 or userSelectedTruck > len(userTruck.options):
                        print("Invalid number")
                    
                    if userSelectedTruck == 1:
                        userTruckSize = userTruck.options[0]["MaxBoxes"]
                        print("\nYou have selected " + userTruck.options[0]["Size"] + " " + userTruck.options[0]["Type"])
                        print("Please note the Truck max stack is : ", userTruckSize)

                        while True:
                            userOptions = input("\nPress 1 to stack item\npress 2 to remove the top item\nPress 3 to redo\nPress 'x' to finish and exit\n")

                            if userOptions.lower() == "x":
                                userFinish = True
                                break
                            
                            if int(userOptions) == 1:
                                while True:
                                    if userTruckSize == tStack.size:
                                        print("Warning: You have reach maximum stack for this truck, press x to exit, don't try to add more")

                                    things = input("\nWhat would you like to add? press 'x' to exit\n")
                                    if things.lower() == "x":
                                        break
                                    if things.strip() == "":
                                        print("You can't add emptiness..")
                                        continue
                                    if tStack.size >= userTruckSize:
                                        print("Stack overflowed!")
                                        break

                                    tStack.push(things.strip())  
                                    print("You have added ", things)  
                                    print("Current Stack")
                                    tStack.traverse()
                            
                            if int(userOptions) == 2:
                                try:
                                    tStack.pop()
                                    print(tStack.removedNode.dataValue, "has been removed")
                                    print("Current Stack")
                                    tStack.traverse()
                                    continue
                                except:
                                    continue

                            if int(userOptions) == 3:
                                tStack.redo()
                                print("Last item has been put back on top")
                                print("Current Stack")
                                tStack.traverse()
                                continue
                       
                    if userSelectedTruck == 2:
                        userTruckSize = userTruck.options[1]["MaxBoxes"]
                        print("\nYou have selected " + userTruck.options[1]["Size"] + " " + userTruck.options[1]["Type"])
                        print("Please note the Truck max stack is : ", userTruckSize)

                        while True:
                            userOptions = input("\nPress 1 to stack item\npress 2 to remove the top item\nPress 3 to redo\nPress 'x' to finish and exit\n")

                            if userOptions.lower() == "x":
                                userFinish = True
                                break
                            
                            if int(userOptions) == 1:
                                while True:
                                    if userTruckSize == tStack.size:
                                        print("You have reach maximum stack for this truck, press x to exit, don't try to add more")

                                    things = input("\nWhat would you like to add? press 'x' to exit\n")
                                    if things.lower() == "x":
                                        break
                                    if things.strip() == "":
                                        print("You can't add emptiness..")
                                        continue
                                    if tStack.size >= userTruckSize:
                                        print("Stack overflowed!")
                                        break

                                    tStack.push(things.strip())  
                                    print("You have added ", things)  
                                    print("Current Stack")
                                    tStack.traverse()
                            
                            if int(userOptions) == 2:
                                try:
                                    tStack.pop()
                                    print(tStack.removedNode.dataValue, "has been removed")
                                    print("Current Stack")
                                    tStack.traverse()
                                    continue
                                except:
                                    continue

                            if int(userOptions) == 3:
                                tStack.redo()
                                print("Last item has been put back on top")
                                print("Current Stack")
                                tStack.traverse()
                                continue
                     
                except ValueError:
                    print("Invalid Input!")
                    continue
            
        elif userInit.lower() == "x":
            break
        else:
            print("Invalid Input")
            continue

    print("\nStacking summary")
    tStack.traverse()

main()