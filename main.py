from food import Food, Node, SLinkedList

def main():
    foodStall = Food()
    newOrderList = SLinkedList()

    def isKeyExist(arr, dict):
        for elem in arr:
            if elem["foodName"] == dict.get("foodName"):
                return True
        return False

    while True:
        customerContinue = True
        customerUniqueOrder = []
        backtoMenu = False
        backtoOrderSummary = False

        orderState = input("Welcome to Wasin's Burger Stack! \nPress 'y' if you would like to order\nPress 'x' to exit the program\n")
        if orderState.lower() == "y":
            while True: 
                pax = input("\nPlease enter how many persons\n")
                try: 
                    pax = int(pax)
                    break
                except ValueError:
                    print("Please enter a number")

            while True:
                backtoMenu = False
                if customerContinue == False:
                    break

                print("\nWhat would you like to order?")

                for elem in foodStall.menuList:
                    print(str(elem["id"])+")", elem["name"], "$" + str(elem["price"]))

                try: 
                    customerSelect = input("Please enter respective food menu number you wish to order, or press 'x' to exit\n")
                    if customerSelect.lower() == "x":
                        break
                    customerSelect = int(customerSelect)

                    if customerSelect <= 0 or customerSelect > len(foodStall.menuList): 
                        print("invalid number\n")
                        continue
               
                    foodName  = foodStall.menuList[customerSelect - 1]["name"]
                    foodPrice = foodStall.menuList[customerSelect - 1]["price"]
                    foodId    = foodStall.menuList[customerSelect - 1]["id"]

                    while True:
                        if backtoMenu == True:
                            break
                        if customerContinue == False:
                            break
                        quantity = input("How many of " + foodName + " would you like? Press 'x' to exit\n") 
                        if quantity.lower() == "x":
                            break
                        try: 
                            quantity = int(quantity)
                            if quantity < 0:
                                print("Please enter a valid number\n")
                                continue

                            confirm = input("Confirm ordering " + str(quantity) + " " + foodName + "?\n" + "Press 'y' fo yes, 'n' for no\n")
                            if confirm.lower() == "y":
                                foodStall.addFood(customerSelect, quantity)
                                orderDict = {"foodName": foodName, "quantity": quantity, "totalPrice": quantity * foodPrice, "id": foodId, "price": foodPrice}
        
                                if isKeyExist(customerUniqueOrder, orderDict):
                                    for elem in customerUniqueOrder:
                                        if elem["foodName"] == orderDict.get("foodName"):
                                            elem["quantity"] += orderDict.get("quantity")
                                            elem["totalPrice"] += orderDict.get("totalPrice")
                                            break
                                else:
                                    customerUniqueOrder.append(orderDict)

                                i = 0
                                while i < quantity:
                                    newOrderList.append(foodName)
                                    i += 1
                                
                            elif confirm.lower() == "n":
                                continue
                            else:
                                print("Invalid input\n")
                                continue

                            while True:  
                                backtoOrderSummary = False     
                                    
                                print("\nYour current order summary")
                                for elem in customerUniqueOrder:
                                    print(str(elem["quantity"]) + " " + elem["foodName"] + " $"+ str(elem["totalPrice"]))
                                print("Total price with tax is ${:.2f}".format(foodStall.totalPriceWithTax()))

                                proceedToPay = input("\nPress 'y' to proceed to payment and exit\nPress 'c' to continue adding your order\nPress 'm' to modify or delete your order\n")

                                if proceedToPay.lower() == "y":
                                    customerContinue = False
                                    break
                                elif proceedToPay.lower() == "c":
                                    backtoMenu = True
                                    break
                                elif proceedToPay.lower() == "m":
                                    while True:
                                        if backtoOrderSummary:
                                            break
                                        print("\nYour current order summary")
                                        for elem in customerUniqueOrder:
                                            print(str(elem["quantity"]) + " " + elem["foodName"] + " $"+ str(elem["totalPrice"]))
                                        print("Total price with tax is ${:.2f}".format(foodStall.totalPriceWithTax()))
                                
                                        print ("\nWhich food number would you like to modify? Press 'x' to exit and see your order")
                                        
                                        i = 1
                                        for elem in customerUniqueOrder:
                                            print(str(i) + ") " + elem["foodName"])
                                            i += 1
                                        customerModify = input()
                                        if customerModify.lower() == "x":
                                            backtoMenu = True
                                            break
                                        try: 
                                            customerModify = int(customerModify)
                                            if customerModify <= 0 or customerModify > len(customerUniqueOrder): 
                                                print("invalid number\n")
                                                continue
                                            while True:
                                                quantity = input("How many of " + customerUniqueOrder[customerModify - 1]["foodName"] + " would you like to change to? Press '0' if you wish to remove\n") 
                                                try:
                                                    quantity = int(quantity)
                                                    if quantity == 0 or quantity == customerUniqueOrder[customerModify - 1]["quantity"]:
                                                        i = 0
                                                        while i < customerUniqueOrder[customerModify - 1]["quantity"]:
                                                            newOrderList.delete(customerUniqueOrder[customerModify - 1]["foodName"])
                                                            i += 1
                                                        foodStall.removeFood(customerUniqueOrder[customerModify - 1]["id"], i)
                                                        customerUniqueOrder.pop(customerModify - 1)
                                                        print("Item has been removed from list")
                                                        backtoOrderSummary = True
                                                        break
                                                    elif quantity < 0:
                                                        print("Invalid Number")
                                                    elif quantity > customerUniqueOrder[customerModify - 1]["quantity"]:
                                                        initialQuantity = customerUniqueOrder[customerModify - 1]["quantity"]
                                                        diff = quantity - initialQuantity 
                                                        i = 0
                                                        while i < diff:
                                                            newOrderList.append(customerUniqueOrder[customerModify - 1]["foodName"])
                                                            foodStall.addFood(customerUniqueOrder[customerModify - 1]["id"], 1)
                                                            i += 1
                                                        amendOrderDict = {"foodName": customerUniqueOrder[customerModify - 1]["foodName"], "quantity": quantity, "totalPrice": quantity * customerUniqueOrder[customerModify - 1]["price"]}
                                                        customerUniqueOrder[customerModify - 1]["quantity"] = amendOrderDict.get("quantity")
                                                        customerUniqueOrder[customerModify - 1]["totalPrice"] = amendOrderDict.get("totalPrice")
                                                        print("Item has been upated accordingly")
                                                        break
                                                    else:
                                                        initialQuantity = customerUniqueOrder[customerModify - 1]["quantity"]
                                                        diff = initialQuantity - quantity
                                                        i = 0
                                                        while i < diff:
                                                            newOrderList.delete(customerUniqueOrder[customerModify - 1]["foodName"])
                                                            foodStall.removeFood(customerUniqueOrder[customerModify - 1]["id"], 1)
                                                            i += 1
                                                        customerUniqueOrder[customerModify - 1]["quantity"] = quantity
                                                        customerUniqueOrder[customerModify - 1]["totalPrice"] = quantity * customerUniqueOrder[customerModify - 1]["price"]
                                                        print("Item has been adjusted accordingly")
                                                        break
                                                
                                                except ValueError:
                                                    print("Please enter a number\n")
                                                    continue

                                        except ValueError:
                                            print("Please enter a number\n")
                                            continue
                        except ValueError:
                            print("Please enter a number\n")
                            continue

                except ValueError:
                    print("Please enter a number\n")
                    continue

            if foodStall.totalPriceWithTax() == 0:
                customerReorder = input("Oh no seems like your cart is empty\nPress 'y' if you would like to order again or press 'x' to exit\n")
                if customerReorder.lower() == "y":
                    continue
                elif customerReorder.lower() == "x":
                    print("We hope to serve you next time!\n")
                    break
                else:
                    print("Invalid input, exiting program")
                    break
            
            if customerSelect != "x":
                print("Your order summary")
                for elem in customerUniqueOrder:
                    print(str(elem["quantity"]) + " " + elem["foodName"] + " $"+ str(elem["totalPrice"]))
                print("\nTotal price with tax is ${:.2f}".format(foodStall.totalPriceWithTax()))
                print("For {} person(s), average per person is ${:.2f}".format(pax, foodStall.averagePerPax(pax)))
                print("Thank you for your order, we hope to see you again!\n")
                print("Extra: Here's your link-list")
                newOrderList.traverse()
                break

        elif orderState.lower() == "x":
            break
        else:
            continue

main()